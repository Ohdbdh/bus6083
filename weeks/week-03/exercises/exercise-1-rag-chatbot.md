# 練習一：RAG 聊天機械人

## 目標
在教大 MaaS 平台上建立一個基於 RAG 的航空客服聊天機械人。

## 前置條件
- 已登入教大 MaaS 平台 (https://maas.eduhk.hk/)
- 已準備一份客服政策文檔（PDF 或 TXT 格式）
- 已閱讀 [notes/04-maas-knowledge-base.md](../notes/04-maas-knowledge-base.md) 和 [notes/05-build-rag-chatbot.md](../notes/05-build-rag-chatbot.md)

## 步驟

### Part A：建立知識庫
1. 進入「數據集」> 點擊「建立」
2. 選擇「文本數據集」> 選擇「Local File」> 上載你的文檔
3. 配置模型：
   - 索引模型：embedding-3 (FREE)
   - 文檔讀取模型：GLM-4-air (FREE)
   - 圖像理解模型：GLM-4v-flash
4. 選擇「分段模式」，分段條件設為 1000
5. 等待處理完成

### Part B：檢索測試
1. 進入「Search Test」標籤
2. 輸入測試問題，例如：「退票政策是什麼？」
3. 檢查檢索結果的相關度分數
4. 嘗試切換搜尋模式（語義 / 全文 / 混合），比較結果差異

### Part C：建立聊天機械人
1. 點擊「+ Create」> 選擇「Simple App」
2. 配置：
   - AI 模型：Deepseek-V4-Flash 或 GLM-4-flash
   - 系統提示詞：使用 [航空客服模板](../templates/system-prompt-airline.md)
   - 數據庫：關聯你在 Part A 建立的知識庫
   - Temperature：0.2
   - Max Tokens：1000

### Part D：測試
使用以下問題測試你的機械人：

| # | 測試問題 | 預期結果 |
|---|----------|----------|
| 1 | 與你文檔相關的問題 | AI 應引用知識庫內容回答 |
| 2 | 知識庫中有明確答案的問題 | AI 應給出準確回答並引用條款 |
| 3 | 與知識庫無關的問題 | AI 應回覆「無法確認此資訊」 |

## 完成標準
- [ ] 知識庫成功建立並可檢索
- [ ] 聊天機械人能正確回答知識庫中的問題
- [ ] 聊天機械人能正確拒絕回答知識庫以外的問題
- [ ] 所有回答均使用繁體中文
