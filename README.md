# BUS6083 — Week 03：RAG、負責任使用 & UI 設計

> 📅 課堂週次：Week 03  
> 🎯 主題：RAG, Responsible Use & UI 設計  
> 🏫 平台：教大 MaaS (https://maas.eduhk.hk/)  
> 📎 原始簡報：[`assets/week-03-rag-responsible-use-ui-design.pdf`](./assets/week-03-rag-responsible-use-ui-design.pdf)

---

## 📖 課程導覽

本週涵蓋三大核心模組，建議按順序學習：

| # | 模組 | 內容 | 速查入口 |
|---|------|------|----------|
| 1 | RAG 概述 | LLM 幻覺、RAG 定義、開卷考試比喻、價值與審計 | [📖 RAG 概述](docs/01-rag-overview.md) |
| 2 | 負責任使用 | Klarna 案例、Air Canada 案例、人機協作 | [📖 負責任使用](docs/02-responsible-use.md) |
| 3 | 教大 MaaS 平台指南 | 登入、配額、數據集建立、模型配置、檢索測試 | [📖 MaaS 指南](docs/03-eduhk-maas-guide.md) |
| 4 | 聊天機械人構建 | 模型參數、系統提示詞、實際測試 | [📖 聊天機械人構建](docs/04-chatbot-build.md) |
| 5 | Chatflow 風控架構 | 意圖分類、RAG 路徑、固定回復、安全防禦 | [📖 Chatflow 風控](docs/05-chatflow-risk-control.md) |
| 6 | 安全風險 | 越獄攻擊、上下文繞過、本地部署 | [📖 安全風險](docs/06-security.md) |
| 7 | UI/UX & Vibe Coding | UI/UX 基礎、Gemini Canvas、Prompt 模板 | [📖 UI/UX & Vibe Coding](docs/07-ui-ux-vibe-coding.md) |

---

## 🛠️ 實用模板速查

| 模板 | 用途 | 連結 |
|------|------|------|
| 航空客服系統提示詞 | RAG 客服機械人 System Prompt 範例 | [📄 模板](templates/system-prompt-airline.md) |
| 網站生成 — 簡短模板 | 快速生成網站的 Prompt | [📄 模板](templates/website-short-template.md) |
| 網站生成 — 完整模板 | 詳細網站生成 Prompt | [📄 模板](templates/website-full-template.md) |
| Chatflow 風控模板 | 意圖分類 + 風險隔離架構 | [📄 模板](templates/chatflow-risk-control-template.md) |

---

## ✏️ 課堂練習

| 練習 | 主題 | 連結 |
|------|------|------|
| 練習 1 | RAG 聊天機械人 | [✏️ 開始](exercises/exercise-1-rag-chatbot.md) |
| 練習 2 | Chatflow 風控架構 | [✏️ 開始](exercises/exercise-2-chatflow-risk-control.md) |
| 練習 3 | UI 原型設計 | [✏️ 開始](exercises/exercise-3-ui-prototype.md) |

---

## 📚 學習目標

完成本週課程後，你將能夠：

1. **理解** LLM 的概率生成機制與幻覺問題
2. **解釋** RAG 的核心概念、價值與審計追溯能力
3. **分析** 真實商業案例（Klarna、Air Canada）中的 AI 責任歸屬
4. **操作** 教大 MaaS 平台建立知識庫與聊天機械人
5. **設計** 系統提示詞，實現負責任的 AI 客服
6. **構建** Chatflow 風控架構，隔離高風險業務
7. **識別** RAG 系統的安全風險與防禦策略
8. **運用** Vibe Coding 與 Gemini Canvas 快速生成 UI 原型

---

## 🔗 快速連結

- 教大 MaaS 平台：https://maas.eduhk.hk/
- Google Gemini：https://gemini.google.com/
- Perplexity AI：https://www.perplexity.ai/
- HTML Color Codes：https://htmlcolorcodes.com/
- UI Prompt Library：https://uipromptlibrary.com/
- UIverse：https://uiverse.io/

---

## 📌 Zoom 上課使用方式

1. **課前預習**：閱讀 `docs/01` 至 `docs/02`，了解 RAG 基礎概念與案例
2. **課中操作**：跟隨 `docs/03` 至 `docs/05` 在 MaaS 平台實作
3. **課中討論**：參考 `docs/02` 中的案例討論問題
4. **課後練習**：完成 `exercises/` 中的三個練習任務
5. **速查模板**：上課時可隨時打開 `templates/` 中的模板複製使用

> 💡 **提示**：每個文檔都設計為獨立可讀，可按需跳轉查閱。
