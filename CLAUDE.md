# Textile Intel - 紡織供應鏈情報追蹤

## 專案狀態：建置中 (2026-04-14)

專案已建立骨架結構，待完成爬蟲實作與 GitHub Actions 設定。

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **股價抓取** | 17 家公司 + 1 檔 ETF，Yahoo Finance | 待設定 |
| **新聞爬蟲** | 待建立，涵蓋 17 家公司 | 待實作 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | 完成 |
| **報告生成** | 每日報告、7 日報告 | 完成 |
| **前端** | D3.js Dashboard、供應鏈圖、事件時間軸 | 完成 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 待設定 |

### 維護檢查清單

```bash
# 一鍵健康檢查
./scripts/health_check.sh

# 或手動檢查個別項目：
gh run list --limit 5                          # GitHub Actions 狀態
ls -la data/events/$(date +%Y-%m-%d).jsonl     # 今日事件
```

---

## 標準流程

```
fetch_news.py
    |
    +---> data/raw/{date}/news.jsonl    (原始抓取資料)
    |
    +---> enrich_event.py
            |
            +---> data/events/{date}.jsonl  (標準格式，唯一資料源)
                    |
                    +---> generate_metrics.py   -> data/metrics/{date}.json
                    +---> detect_anomalies.py   -> data/metrics/{date}.json (追加異常)
                    +---> generate_daily.py     -> reports/daily/{date}.md
                    +---> generate_7d_report.py -> reports/7d/{date}.md
                    +---> update_baselines.py   -> data/baselines/*.json
```

## 追蹤範圍

- **公司**：17 家紡織供應鏈公司 + 1 檔 ETF
- **主題**：6 個追蹤主題
- **供應鏈**：上游（原料/設備）-> 中游（製造）-> 下游（品牌/通路）

## 設定檔

| 檔案 | 說明 |
|------|------|
| `configs/companies.yml` | 公司清單、供應鏈關係、ETF |
| `configs/topics.yml` | 追蹤主題與關鍵字 |
| `configs/sentiment_rules.yml` | 情緒分析規則 |
| `configs/importance_rules.yml` | 重要性評分規則 |
| `configs/anomaly_rules.yml` | 異常偵測規則 |


---

## 每日例行（進入此 repo 時自動提醒）

當你讀取此 CLAUDE.md 時，主動執行以下檢查並提醒用戶：

### 自動檢查清單

1. **同步最新** — `git pull origin main`
2. **今日 Actions 狀態** — `gh run list --limit 1`
3. **今日事件數** — `wc -l data/events/$(date +%Y-%m-%d).jsonl`
4. **關鍵字審計** — 讀取 `site/data/reports/daily/$(date +%Y-%m-%d).json` 的 `filter_audit` 欄位

### 提醒格式

```
📋 每日狀態
- Actions: ✅/❌
- 今日事件: N 筆
- 關鍵字審計: ✅ 通過 / ⚠️ gate2 擋住率 XX%，建議檢視
```

若 `filter_audit.alert` 為 true 或 `gate2_block_rate > 30%`，提醒用戶：「有關鍵字需要調整，要執行關鍵字審計嗎？」

### 關鍵字審計流程（用戶確認後執行）

1. 檢視 `filter_audit.gate2_samples` 中被擋住的文章標題
2. 判斷每篇是否與本追蹤產業相關
3. 相關的文章 → 找出缺少的關鍵字，建議新增到 `configs/topics.yml`
4. 呈現結果：

```
## 關鍵字審計結果

通過率：XX% | Gate 2 擋住率：XX%

### 被擋住但應通過的文章
| 標題 | 缺少的關鍵字 | 建議加入的主題 |
|------|-------------|--------------|

### 建議新增關鍵字
topics.yml → {topic_id} → keywords 新增：
- keyword1
- keyword2
```

5. 用戶確認後更新 `configs/topics.yml`，commit + push

