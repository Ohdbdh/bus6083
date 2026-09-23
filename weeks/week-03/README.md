# Week 03：RAG、負責任使用 & UI 設計

## 本週核心問題

> 企業想用 AI 做客服，但 LLM 會「幻覺」——我們如何讓 AI 回答既有事實依據、又能追溯來源，同時確保高風險業務不被 AI 擅自處理？

## 本週最終產出

完成本週後，你將擁有：

- ✅ 一個 RAG 知識庫（教大 MaaS 平台）
- ✅ 一個能基於知識庫回答、會誠實拒答的 RAG 客服聊天機械人
- ✅ 一個帶意圖分類器、高風險硬隔離的 Chatflow
- ✅ 一個客服 UI 原型（展示引用來源 + 轉人工入口）

## 三段式學習地圖

本週 8 篇筆記按三個階段展開，從「為什麼」到「怎麼做」到「如何安全交付」：

### Part A：為什麼需要 RAG？（Notes 1–3）

| 筆記 | 核心問題 | 連結 |
|------|----------|------|
| 1. 商業動機 | 企業為什麼迫切需要 AI 客服？Klarna 案例帶來什麼啟示？ | [📖 閱讀](notes/01-business-motivation.md) |
| 2. LLM 幻覺與風險 | 為什麼不能直接讓 LLM 自由回答？Air Canada 為何敗訴？ | [📖 閱讀](notes/02-llm-hallucination-risk.md) |
| 3. RAG 解決方案 | RAG 如何讓 AI「有憑有據」地回答？ | [📖 閱讀](notes/03-rag-solution.md) |

### Part B：如何做出來？（Notes 4–6）

| 筆記 | 核心問題 | 連結 |
|------|----------|------|
| 4. MaaS 與知識庫 | 如何在教大 MaaS 平台建立知識庫？ | [📖 閱讀](notes/04-maas-knowledge-base.md) |
| 5. 構建 RAG 聊天機械人 | 如何設定系統提示詞與模型參數？ | [📖 閱讀](notes/05-build-rag-chatbot.md) |
| 6. Chatflow 風控架構 | 如何隔離高風險業務、防止 AI 越權？ | [📖 閱讀](notes/06-chatflow-risk-control.md) |

### Part C：如何安全地交付給使用者？（Notes 7–8）

| 筆記 | 核心問題 | 連結 |
|------|----------|------|
| 7. 安全與負責任使用 | 上線前還有哪些風險需要排查？ | [📖 閱讀](notes/07-security-responsible-use.md) |
| 8. UI/UX & Vibe Coding | 如何把安全系統包裝成使用者能正確使用的介面？ | [📖 閱讀](notes/08-ui-ux-vibe-coding.md) |

## 課堂流程對照表

| 時間 | 活動 | 打開哪份筆記 | 學生要做什麼 | 完成檢查 |
|------|------|-------------|-------------|----------|
| 15 min | 導入討論 | Note 1 | 分享自己用過的 AI 客服體驗 | 能說出 Klarna 的三根支柱 |
| 20 min | 案例研討 | Notes 1–2 | 對比 Klarna 與 Air Canada | 能解釋 Air Canada 為何敗訴 |
| 15 min | 概念講解 | Notes 2–3 | 理解 LLM 幻覺機制與 RAG 原理 | 能用開卷考試比喻解釋 RAG |
| 40 min | 平台實作 | Notes 4–5 | 在 MaaS 上建立知識庫與聊天機械人 | 通過 Checkpoint 1–5 |
| 20 min | 進階架構 | Note 6 | 設計 Chatflow 風控流程 | 通過 Checkpoint 6–7 |
| 20 min | UI 實作 | Note 8 | 用 Gemini Canvas 生成客服 UI 原型 | UI 包含引用來源 + 轉人工入口 |

## Zoom 速查入口

上課時不知道該看哪份筆記？按需求查詢：

| 我要…… | 去哪裡 |
|---------|--------|
| 看案例 | Notes 1–2（Klarna + Air Canada） |
| 做知識庫 | Note 4 + Checkpoint 1–4 |
| 寫 Prompt | Note 5 + [航空客服模板](templates/system-prompt-airline.md) |
| 做風控 | Note 6 + [Chatflow 風控模板](templates/chatflow-risk-control-template.md) |
| 做 UI 原型 | Note 8 + [網站完整模板](templates/website-full-template.md) |
| 查術語 | [課程術語表](../shared/glossary.md) |

## 實用模板

| 模板 | 用途 | 連結 |
|------|------|------|
| 航空客服系統提示詞 | RAG 客服機械人 System Prompt 範例 | [📄 模板](templates/system-prompt-airline.md) |
| 網站生成 — 簡短模板 | 快速生成網站的 Prompt | [📄 模板](templates/website-short-template.md) |
| 網站生成 — 完整模板 | 詳細網站生成 Prompt | [📄 模板](templates/website-full-template.md) |
| Chatflow 風控模板 | 意圖分類 + 風險隔離架構 | [📄 模板](templates/chatflow-risk-control-template.md) |

## 課堂練習

| 練習 | 主題 | 連結 |
|------|------|------|
| 練習一 | RAG 聊天機械人 | [✏️ 開始](exercises/exercise-1-rag-chatbot.md) |
| 練習二 | Chatflow 風控架構 | [✏️ 開始](exercises/exercise-2-chatflow-risk-control.md) |
| 練習三 | UI 原型設計 | [✏️ 開始](exercises/exercise-3-ui-prototype.md) |

## 本週關鍵詞

RAG · Hallucination · Knowledge Cutoff · Embedding · Hybrid Search · System Prompt · Intent Classifier · Human-in-the-Loop · Jailbreak · Vibe Coding

## 原始簡報

完整原始幻燈片 PDF：[`assets/week-03-rag-responsible-use-ui-design.pdf`](assets/week-03-rag-responsible-use-ui-design.pdf)
