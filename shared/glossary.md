# 課程術語表

## LLM 相關

| 術語 | 英文 | 解釋 |
|------|------|------|
| 大型語言模型 | Large Language Model (LLM) | 基於 Transformer 架構、在海量文本上訓練的深度學習模型 |
| Token | Token | 模型處理文本的基本單位，約等於一個詞或字 |
| 幻覺 | Hallucination | 模型以篤定口吻生成與事實不符的內容 |
| 知識截斷 | Knowledge Cutoff | LLM 的知識停留在訓練數據收集完成的那一刻 |
| 概率預測 | Probabilistic Prediction | 模型逐一預測最可能出現的下一個 Token |
| RLHF | Reinforcement Learning from Human Feedback | 人類反饋強化學習，用於對齊模型行為 |

## RAG 相關

| 術語 | 英文 | 解釋 |
|------|------|------|
| 檢索增強生成 | Retrieval-Augmented Generation (RAG) | 從外部知識庫動態檢索資訊，增強 LLM 輸出準確度 |
| 向量嵌入 | Embedding | 將文本轉換為數值向量，支援語義檢索 |
| 語義搜尋 | Semantic Search | 依據概念意涵進行比對，而非關鍵字匹配 |
| 混合搜尋 | Hybrid Search | 結合語義比對與關鍵字檢索 |
| 結果重排 | Re-Rank | 對初步檢索結果進行二次相關度評分 |
| 分段模式 | Chunk Mode | 將文檔拆解為均勻的語義段落 |
| 問答對模式 | QA Pair Mode | 由 AI 預先將內容提煉為一問一答形式 |
| 引註 | Citation | 標註回答所依據的原文來源 |

## 模型參數

| 術語 | 英文 | 解釋 |
|------|------|------|
| 最大生成長度 | Max Tokens | 限制模型單次回覆的最大長度 |
| 溫度值 | Temperature | 控制生成的隨機度；低=嚴謹，高=創意 |
| 核採樣值 | Top_p | 在累積概率達到門檻的詞彙中抽樣，典型值 0.9–0.95 |
| 系統提示詞 | System Prompt | 設定模型角色、規範與限制，權限高於用戶輸入 |
| 用戶提示詞 | User Prompt | 用户即時輸入的查詢或任務 |

## Chatflow 相關

| 術語 | 英文 | 解釋 |
|------|------|------|
| 工作流 | Workflow | 預先定義的、按步驟執行的任務序列 |
| 意圖分類器 | Intent Classifier | 自動判別用户問題類型的節點 |
| 指定回復 | Specified Response | 輸出固定內容的節點，用於高風險路徑 |
| 硬隔離 | Hard Isolation | 高風險業務強制繞過 LLM，轉人工或固定表單 |
| Human-in-the-Loop | Human-in-the-Loop | AI 負責標準件，人類負責複雜件的人機協作架構 |

## UI/UX 相關

| 術語 | 英文 | 解釋 |
|------|------|------|
| 使用者介面 | User Interface (UI) | 應用程式的外觀：顏色、字型、佈局、按鈕 |
| 使用者體驗 | User Experience (UX) | 應用程式的使用感受：易用性、邏輯清晰度、流暢度 |
| Vibe Coding | Vibe Coding | 用自然語言描述需求，由 AI 生成程式碼 |
| 響應式設計 | Responsive Design | 自動適配不同螢幕尺寸的網頁設計 |
