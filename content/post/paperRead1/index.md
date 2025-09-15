---
title: 生醫文摘-Dysregulated RNA splicing impairs regeneration in alcohol-associated liver disease
date: 2025-09-14
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## 文章標題
[Dysregulated RNA splicing impairs regeneration in alcohol-associated liver disease](https://www.nature.com/articles/s41467-025-63251-2#Sec10)

---
## 文章概要
這篇研究聚焦於為何 `酒精相關肝病（ALD）` 患者在停酒後仍常出現`再生失靈`、走向肝衰竭。作者整合 `單核轉錄體（snRNA-seq）與染色質可及性（snATAC-seq）` 的`多體學`，以及RNA-seq，比較 `健康`、`嚴重酒精性肝炎（SAH）`、`酒精性肝硬化（AC）` 的人類肝臟。結果顯示：ALD 中的免疫環境改變，伴隨成人肝細胞失去成熟身分、卻無法成功轉入可增殖的前驅狀態。同時，`RNA 結合蛋白（RBP）`表現 受到擾動，特別是 `ESRP2` 顯著下調，造成廣泛的選擇性剪接異常。這些錯剪事件之一會讓 TCF4 與 SLK 遺失核定位訊號外顯子，導致蛋白質由核內轉為細胞質，進一步擾動 WNT / Hippo 等對肝再生關鍵的路徑。作者也在細胞與小鼠模型中操作這些剪接事件（反義寡核苷酸、`TGF-β `作用等）驗證致病意義，並指出 `TGF-β 上升` 會抑制 ESRP2 的上皮型剪接程式。整體而言，錯剪 RNA 既可作為 ALD 生物標記，也可能是可介入的治療標的。

---
## 技術探討
這篇用兩個關鍵工具把「剪接事件 → 功能影響 → 誰在調控」串成一條線：`Exon Ontology` 先把 `rMATS` 找到的`顯著可變外顯子（ΔPSI）`翻譯成蛋白層級的功能語意（例如是否含核定位訊號 NLS、是否落在功能域/無序區、是否覆蓋磷酸化位點等），直接指出哪些錯剪最可能改變蛋白定位或活性；接著用 `eCLIP（enhanced Crosslinking and ImmunoPrecipitation）`去驗證「是誰」在這些外顯子附近施加調控：其原理是以 UV（常用 254 nm）把 RNA 與其結合的 RBP 共價交聯，然後用特異性抗體（如 FLAG-ESRP2）將 RBP–RNA 複合體免疫沉澱，經去蛋白與建庫後定序，再尋找`峰值（peaks）`與 `交聯誘發突變/截斷（CIMS/CITS）`，把 RBP 的結合位點精確到核苷酸附近；當這些 eCLIP 訊號在「外顯子本體論」標註為關鍵功能的外顯子上下游富集時，就能從事件（錯剪）→ 功能（如 NLS 流失致核→質轉位）→ 調控者（ESRP2 直接結合）給出具體且可實驗驗證的機制證據。

> 「顯著可變外顯子（ΔPSI）」指的是：在兩組條件（例如疾病 vs 對照）之間，某個可變剪接事件的外顯子納入比例（PSI, Percent Spliced In）發生了具有統計意義的改變。PSI 近似可寫為：PSI =（支持「外顯子被納入」的接點讀數）/（納入讀數 + 跳過讀數）；而 ΔPSI = PSI_案例 − PSI_對照，因此 ΔPSI > 0 表示該外顯子在案例更常被納入，ΔPSI < 0 則更常被跳過。常見用 rMATS 等工具，對各類事件（SE：外顯子跳躍、RI：內含子保留、A5SS/A3SS：5'/3' 端可變剪接、MXE：互斥外顯子）估計 PSI，並以多重校正後的 FDR 門檻（如 FDR < 0.05 或 0.1）、最小接點讀數（Junction read out, 如 ≥10）及 |ΔPSI| 門檻（如 ≥0.1，即 10% 變化）來定義「Differential splicing」。在這篇文脈中，先用 ΔPSI 找出「真的剪接有變」的外顯子，再用 Exon Ontology 判斷這些外顯子是否包含功能關鍵元素（如 NLS、功能域、PTM 位點），最後再用 eCLIP 檢查調控該事件的 RBP 是否在該外顯子附近有直接結合證據。