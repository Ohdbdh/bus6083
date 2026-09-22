# Week 03：RAG、負責任使用 & UI 設計

## 本週核心問題

> 企業想用 AI 做客服，但 LLM 會「幻覺」——我們如何讓 AI 回答既有事實依據、又能追溯來源，同時確保高風險業務不被 AI 擅自處理？

## 學習路徑

本週按以下敘事線展開，從「為什麼」到「怎麼做」：

| 順序 | 主題 | 核心問題 | 連結 |
|------|------|----------|------|
| 1 | 商業動機：為什麼企業需要 AI 客服 | 市場數據與 Klarna 案例帶來什麼啟示 | [📖 閱讀](notes/01-business-motivation.md) |
| 2 | 問題根源：LLM 幻覺與商業風險 | 為什麼不能直接讓 LLM 自由回答 | [📖 閱讀](notes/02-llm-hallucination-risk.md) |
| 3 | RAG 作為解決方案 | RAG 如何讓 AI 「有憑有據」地回答 | [📖 閱讀](notes/03-rag-solution.md) |
| 4 | 實作準備：MaaS 平台與知識庫 | 如何在教大 MaaS 平台建立知識庫 | [📖 閱讀](notes/04-maas-knowledge-base.md) |
| 5 | 實作：構建 RAG 聊天機械人 | 如何設定系統提示詞與模型參數 | [📖 閱讀](notes/05-build-rag-chatbot.md) |
| 6 | 進階：Chatflow 風控架構 | 如何隔離高風險業務、防止 AI 越權 | [📖 閱讀](notes/06-chatflow-risk-control.md) |
| 7 | 安全與負責任使用 | 越獄攻擊、本地部署、人機協作 | [📖 閱讀](notes/07-security-responsible-use.md) |
| 8 | UI/UX & Vibe Coding | 如何用自然語言快速生成 UI 原型 | [📖 閱讀](notes/08-ui-ux-vibe-coding.md) |

## 課堂活動順序

1. **導入討論**（15 min）— 你用過哪些 AI 客服？體驗如何？
2. **案例研討**（20 min）— Klarna 與 Air Canada 對比討論
3. **概念講解**（15 min）— LLM 幻覺機制與 RAG 原理
4. **平台實作**（40 min）— 在 MaaS 上建立知識庫與聊天機械人
5. **進階架構**（20 min）— Chatflow 風控設計
6. **UI 實作**（20 min）— Gemini Canvas 網站生成

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

## 原始簡報

完整原始幻燈片 PDF：[`assets/week-03-rag-responsible-use-ui-design.pdf`](assets/week-03-rag-responsible-use-ui-design.pdf)
