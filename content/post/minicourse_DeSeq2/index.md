---
title: 迷你課程:R語言生物資訊實作~Bulk RNA-seq分析-2
date: 2025-08-23
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言生物資訊實作]
tags: [R,coding, bioinformatics]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
為什麼設計公式決定了分析成敗？
很多研究人員常常忽略一個事實：RNA-seq 分析出錯最常見的地方，不在於統計模型本身，而是在於 如何將生物學問題正確轉換成統計語言。
在 DESeq2 中，`設計公式（design formula）`就像是一張藍圖，它告訴程式：
- 你的生物問題是什麼
- 你想比較哪些條件
- 又要如何處理實驗中的雜訊與批次效應
如果設計正確，DESeq2 會給你清晰可靠的結果；若設計錯誤，即使你的實驗做得完美，分析也可能得出錯誤結論。
好消息是：只要理解設計公式背後的邏輯，選擇正確的模型其實非常直觀。

---
## 設計公式的三大功能
1. 指出哪些因子會影響基因表現（如處理條件、基因型、`批次`等）
2. 定義你想比較的條件（例如`「處理組 vs 對照組」`）
3. 控制潛在混雜變數（如批次效應、個體差異）

設計公式的一般格式為：
```r
design = ~ confounders + biological_factors
```

## 常見的實驗設計範例
#### 1. 簡單兩組比較
場景：單純比較處理組與對照組
```r
design = ~ condition
results(dds, contrast = c("condition", "treated", "control")) #contrast 放: 要比較哪個因子，這個因子裡面的哪兩個需要比較？
```
- 適用：只有一個研究因子的乾淨實驗。

#### 2. 多組條件比較
場景：多種處理與對照比較
```r
design = ~ treatment
results(dds, contrast = c("treatment", "drugA", "control"))
results(dds, contrast = c("treatment", "drugB", "control"))
results(dds, contrast = c("treatment", "drugA", "drugB"))
```
- 適用：多藥物比較、劑量反應、時間序列實驗。

#### 3. 配對/重複測量設計
場景：同一位病人`治療前後的樣本`
```r
design = ~ patient + condition
```
作用：
- 消除個體差異影響
- 專注於治療效果
- 能大幅提升統計效能

#### 4. 批次效應校正
場景：樣本在不同天數或不同人處理
```r
#常用
design = ~ batch + condition
```
作用：
- 抑制技術性差異
- 更準確評估生物學效果
- `幾乎所有實驗都建議納入批次因子`

#### 5. 因子交互作用設計
場景：想檢驗不同因子之間是否有交互作用
```r
design = ~ genotype + treatment + genotype:treatment
```
作用：
- 主要效應：基因型差異
- 主要效應：處理差異
- 交互作用：不同基因型對治療的反應是否不同
在 DESeq2 中，若設計公式包含交互作用，模型會`同時估計主效應與交互作用效應`；透過 `resultsNames(dds)` 可以找到交互作用項（如 genotypeKO.treatmentdrug），並用 `results(dds, name="genotypeKO.treatmentdrug")` 提取結果，取得 log2FC、p 值與 padj。
若交互作用顯著，`表示 treatment 效果會依 genotype 而異，此時主效應不能單獨解讀`，必須關注不同組合下的差異並搭配圖表呈現。

---
## 設計公式的實用原則
順序很重要
混雜因子要放在前面，感興趣的生物因子放在最後：
```r
# 正確
design = ~ batch + sex + treatment

# 錯誤
design = ~ treatment + batch + sex
```
保持簡單
- 小樣本只適合簡單設計
- 複雜設計需要更多重複數才能保證結果穩健
建議樣本數：
設計類型	最低需求	建議數量
簡單 (~ condition)	≥3	5–6
含批次 (~ batch + cond.)	≥3	4–5
因子交互 (~ A + B + A:B)	≥3/組合	5–6/組合
時間序列 (~ time)	≥3/時間點	4–5/時間點

## 計數矩陣的最佳實踐
移除低表達基因
```r
keep <- rowSums(counts(dds)) >= 10
dds_filtered <- dds[keep, ]
```
好處：減少噪音，提高統計檢出力。

## 正確設定參考組
```r
levels(dds$condition)            # 查看順序
dds$condition <- relevel(dds$condition, ref = "control")
levels(dds$condition)            # 確認 control 在第一位
```
- 影響：正確解讀正負 fold change 的方向。

> 常見錯誤與解法

> 忽略批次效應

> 問題：樣本可能按照處理日期聚集，而不是生物條件

> 解法：加上批次因子

> design = ~ batch + condition

> 設計過於複雜
> 問題：因子太多、樣本太少 → 結果不穩定
> 解法：先用簡單模型，再逐步增加複雜度
> 錯誤的參考組
> 問題：DESeq2 預設按字母排序
> 解法：手動指定 control 為參考組

## 實際應用案例
時間序列實驗
design = ~ time
每個時間點至少 3–5 個生物重複
臨床試驗（含批次）
design = ~ batch + sex + treatment
控制技術差異與性別影響，聚焦治療效果
藥物組合實驗
design = ~ drugA + drugB + drugA:drugB
檢驗單藥效應與交互作用（協同或拮抗）

## 完整流程範例
# 1. 建立 DESeq2 對象
dds <- DESeqDataSetFromMatrix(counts, colData = metadata, design = ~ 1)

# 2. 檢查實驗因子
table(dds$condition)
table(dds$batch)

# 3. 設定參考組
dds$condition <- relevel(dds$condition, ref = "control")

# 4. 指定設計公式
design(dds) <- ~ batch + condition

# 5. 移除低表達基因
keep <- rowSums(counts(dds)) >= 10
dds <- dds[keep, ]

# 6. 驗證
print(dds)
print(design(dds))
print(levels(dds$condition))
完成以上步驟後，就可以進入 DESeq2 的差異分析流程。