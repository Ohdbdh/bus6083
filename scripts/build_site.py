#!/usr/bin/env python3
"""Convert markdown files to HTML pages with shared layout for the course site."""
import re
import os
import html
from pathlib import Path

BASE = Path("/home/user/workspace/bus6083-week03")
SITE = BASE / "site"

# ---- Markdown to HTML converter ----

def md_to_html(md):
    lines = md.split('\n')
    result = []
    i = 0
    in_table = False
    table_rows = []
    in_code = False
    code_lines = []
    
    def flush_table():
        nonlocal table_rows, in_table
        if not table_rows:
            return ''
        out = ['<table>']
        for idx, row in enumerate(table_rows):
            cells = [c.strip() for c in row.split('|')]
            cells = [c for c in cells if c != '']
            if idx == 1 and all(re.match(r'^[-:]+$', c) for c in cells):
                continue
            tag = 'th' if idx == 0 else 'td'
            out.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells) + '</tr>')
        out.append('</table>')
        table_rows = []
        in_table = False
        return '\n'.join(out)
    
    def inline(text):
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
        return text
    
    while i < len(lines):
        line = lines[i]
        
        if line.strip().startswith('```'):
            if in_code:
                result.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')
                code_lines = []
                in_code = False
            else:
                if in_table:
                    result.append(flush_table())
                in_code = True
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        
        if '|' in line and line.strip().startswith('|'):
            in_table = True
            table_rows.append(line.strip())
            i += 1
            continue
        elif in_table:
            result.append(flush_table())
        
        if line.startswith('# ') and not line.startswith('## '):
            result.append(f'<h1>{inline(line[2:].strip())}</h1>')
        elif line.startswith('## '):
            result.append(f'<h2>{inline(line[3:].strip())}</h2>')
        elif line.startswith('### '):
            result.append(f'<h3>{inline(line[4:].strip())}</h3>')
        elif line.startswith('> '):
            bq_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                bq_lines.append(lines[i][2:].strip())
                i += 1
            result.append(f'<blockquote>{inline(" ".join(bq_lines))}</blockquote>')
            continue
        elif line.strip() == '---':
            result.append('<hr>')
        elif re.match(r'^[\s]*[-*]\s+\[[ xX]\]\s+', line):
            # Checkbox list item
            checked = ' checked' if '[x]' in line.lower() or '[X]' in line else ''
            text = re.sub(r'^[\s]*[-*]\s+\[[ xX]\]\s+', '', line)
            result.append(f'<div class="checkbox-item"><input type="checkbox"{checked} disabled> {inline(text)}</div>')
        elif re.match(r'^[\s]*[-*]\s+', line):
            result.append(f'<li>{inline(re.sub(r"^[\s]*[-*]\s+", "", line))}</li>')
        elif re.match(r'^\d+\.\s+', line):
            result.append(f'<li>{inline(re.sub(r"^\d+\.\s+", "", line))}</li>')
        elif line.strip() == '':
            result.append('')
        else:
            result.append(f'<p>{inline(line.strip())}</p>')
        i += 1
    
    if in_table:
        result.append(flush_table())
    if in_code:
        result.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')
    
    # Wrap loose <li> in <ul>
    html_text = '\n'.join(result)
    html_text = re.sub(r'(<li>.*?</li>\n?)+', lambda m: f'<ul>{m.group(0)}</ul>', html_text, flags=re.DOTALL)
    return html_text


SIDEBAR_LINKS = [
    ("notes/01-business-motivation.html", "1", "商業動機"),
    ("notes/02-llm-hallucination-risk.html", "2", "LLM 幻覺與風險"),
    ("notes/03-rag-solution.html", "3", "RAG 解決方案"),
    ("notes/04-maas-knowledge-base.html", "4", "MaaS 與知識庫"),
    ("notes/05-build-rag-chatbot.html", "5", "構建 RAG 聊天機械人"),
    ("notes/06-chatflow-risk-control.html", "6", "Chatflow 風控"),
    ("notes/07-security-responsible-use.html", "7", "安全與負責任使用"),
    ("notes/08-ui-ux-vibe-coding.html", "8", "UI/UX & Vibe Coding"),
]

TEMPLATE_LINKS = [
    ("templates/system-prompt-airline.html", "航空客服提示詞"),
    ("templates/website-short-template.html", "網站簡短模板"),
    ("templates/website-full-template.html", "網站完整模板"),
    ("templates/chatflow-risk-control-template.html", "Chatflow 風控模板"),
]

EXERCISE_LINKS = [
    ("exercises/exercise-1-rag-chatbot.html", "練習一：RAG 聊天機械人"),
    ("exercises/exercise-2-chatflow-risk-control.html", "練習二：Chatflow 風控"),
    ("exercises/exercise-3-ui-prototype.html", "練習三：UI 原型設計"),
]


def make_page(title, body_html, active_id=None):
    """Generate HTML page with shared sidebar layout.
    
    Pages are generated at site/weeks/week-03/{notes,templates,exercises}/*.html
    That's 3 levels deep from site root, so:
    - Assets (CSS/JS) need ../../../ prefix
    - Site root index needs ../../../ prefix  
    - Week-03 index needs ../ prefix (same level as notes/templates/exercises)
    - Sibling pages (other notes, templates, exercises) need ../ prefix + subfolder
    """
    ASSET = "../../../"  # to reach site/ root (assets/, index.html)
    PAGE = "../"         # to reach weeks/week-03/ (index.html, and subfolders)
    
    def make_link(href, num, label, active_id):
        cls = ' class="sidebar-link active"' if active_id == href else ' class="sidebar-link"'
        num_html = f'<span class="sidebar-link-num">{num}</span>' if num else ''
        return f'<a href="{PAGE}{href}"{cls}>{num_html}{label}</a>'
    
    module_links = '\n'.join(make_link(h, n, l, active_id) for h, n, l in SIDEBAR_LINKS)
    template_links = '\n'.join(make_link(h, None, l, active_id) for h, l in TEMPLATE_LINKS)
    exercise_links = '\n'.join(make_link(h, None, l, active_id) for h, l in EXERCISE_LINKS)
    
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — BUS6083 Week 03</title>
  <meta name="description" content="{title} — BUS6083 Week 03 課程知識庫">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{ASSET}assets/style.css">
  <link rel="stylesheet" href="{ASSET}assets/layout.css">
</head>
<body>
  <div class="sidebar-overlay"></div>
  <div class="page-layout">
    <aside class="sidebar">
      <a href="{ASSET}index.html" class="sidebar-brand">
        <div class="sidebar-brand-icon">B</div>
        <div class="sidebar-brand-text">
          <span class="sidebar-brand-title">BUS6083</span>
          <span class="sidebar-brand-sub">課程知識庫</span>
        </div>
      </a>
      <div class="sidebar-section">
        <div class="sidebar-section-title">Week 03 學習路徑</div>
        {module_links}
      </div>
      <div class="sidebar-section">
        <div class="sidebar-section-title">模板與練習</div>
        {template_links}
        {exercise_links}
      </div>
      <div class="sidebar-section">
        <div class="sidebar-section-title">外部資源</div>
        <a href="https://github.com/Ohdbdh/bus6083" target="_blank" rel="noopener" class="sidebar-link">GitHub 倉庫</a>
        <a href="https://maas.eduhk.hk/" target="_blank" rel="noopener" class="sidebar-link">教大 MaaS 平台</a>
        <a href="https://gemini.google.com/" target="_blank" rel="noopener" class="sidebar-link">Google Gemini</a>
      </div>
    </aside>

    <div class="main">
      <header class="header">
        <div class="header-left">
          <button class="header-menu-btn" data-menu-toggle aria-label="開啟選單">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
          </button>
          <span class="header-title">{title}</span>
        </div>
        <div class="header-right">
          <a href="https://github.com/Ohdbdh/bus6083" target="_blank" rel="noopener" class="header-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.4.5 0 5.9 0 12.5c0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2 0-.4-.5-1.5.2-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.7.2 2.8.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 24 12.5C24 5.9 18.6.5 12 .5z"/></svg>
            GitHub
          </a>
          <button class="theme-toggle" data-theme-toggle aria-label="切換深淺色模式">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          </button>
        </div>
      </header>

      <main class="content">
        <a href="{PAGE}index.html" class="article-back">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          返回 Week 03
        </a>
        <div class="article-header">
          <h1 class="article-title">{title}</h1>
        </div>
        <div class="article-body">
{body_html}
        </div>
      </main>

      <footer class="footer">
        BUS6083 · Week 03 · 課程知識庫<br>
        <a href="https://github.com/Ohdbdh/bus6083" target="_blank" rel="noopener" style="color:var(--color-text-faint)">GitHub 倉庫</a>
      </footer>
    </div>
  </div>
  <script src="{ASSET}assets/app.js"></script>
</body>
</html>'''


# Notes
notes = [
    ("weeks/week-03/notes/01-business-motivation.md", "notes/01-business-motivation.html", "1. 商業動機：為什麼企業需要 AI 客服"),
    ("weeks/week-03/notes/02-llm-hallucination-risk.md", "notes/02-llm-hallucination-risk.html", "2. 問題根源：LLM 幻覺與商業風險"),
    ("weeks/week-03/notes/03-rag-solution.md", "notes/03-rag-solution.html", "3. RAG 作為解決方案"),
    ("weeks/week-03/notes/04-maas-knowledge-base.md", "notes/04-maas-knowledge-base.html", "4. 實作準備：MaaS 平台與知識庫"),
    ("weeks/week-03/notes/05-build-rag-chatbot.md", "notes/05-build-rag-chatbot.html", "5. 實作：構建 RAG 聊天機械人"),
    ("weeks/week-03/notes/06-chatflow-risk-control.md", "notes/06-chatflow-risk-control.html", "6. 進階：Chatflow 風控架構"),
    ("weeks/week-03/notes/07-security-responsible-use.md", "notes/07-security-responsible-use.html", "7. 部署前安全檢查與治理設計"),
    ("weeks/week-03/notes/08-ui-ux-vibe-coding.md", "notes/08-ui-ux-vibe-coding.html", "8. UI/UX & Vibe Coding：讓安全系統被使用者看見"),
]

for md_path, html_path, title in notes:
    md_content = (BASE / md_path).read_text(encoding='utf-8')
    md_content = re.sub(r'^# .+\n', '', md_content, count=1)
    body = md_to_html(md_content)
    page = make_page(title, body, active_id=html_path)
    (SITE / "weeks" / "week-03" / html_path).write_text(page, encoding='utf-8')
    print(f"  Generated: weeks/week-03/{html_path}")

# Templates
templates = [
    ("weeks/week-03/templates/system-prompt-airline.md", "templates/system-prompt-airline.html", "航空客服系統提示詞"),
    ("weeks/week-03/templates/website-short-template.md", "templates/website-short-template.html", "網站生成 — 簡短模板"),
    ("weeks/week-03/templates/website-full-template.md", "templates/website-full-template.html", "網站生成 — 完整模板"),
    ("weeks/week-03/templates/chatflow-risk-control-template.md", "templates/chatflow-risk-control-template.html", "Chatflow 風控架構模板"),
]

for md_path, html_path, title in templates:
    md_content = (BASE / md_path).read_text(encoding='utf-8')
    md_content = re.sub(r'^# .+\n', '', md_content, count=1)
    body = md_to_html(md_content)
    page = make_page(title, body, active_id=html_path)
    (SITE / "weeks" / "week-03" / html_path).write_text(page, encoding='utf-8')
    print(f"  Generated: weeks/week-03/{html_path}")

# Exercises
exercises = [
    ("weeks/week-03/exercises/exercise-1-rag-chatbot.md", "exercises/exercise-1-rag-chatbot.html", "練習一：RAG 聊天機械人"),
    ("weeks/week-03/exercises/exercise-2-chatflow-risk-control.md", "exercises/exercise-2-chatflow-risk-control.html", "練習二：Chatflow 風控架構"),
    ("weeks/week-03/exercises/exercise-3-ui-prototype.md", "exercises/exercise-3-ui-prototype.html", "練習三：UI 原型設計"),
]

for md_path, html_path, title in exercises:
    md_content = (BASE / md_path).read_text(encoding='utf-8')
    md_content = re.sub(r'^# .+\n', '', md_content, count=1)
    body = md_to_html(md_content)
    page = make_page(title, body, active_id=html_path)
    (SITE / "weeks" / "week-03" / html_path).write_text(page, encoding='utf-8')
    print(f"  Generated: weeks/week-03/{html_path}")

print("\nAll pages generated successfully!")
