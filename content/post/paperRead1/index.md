---
title: 生醫文摘-Dysregulated RNA splicing impairs regeneration in alcohol-associated liver disease
date: 2025-09-14
authors: ["戴揚紘", ""]
commentable: true
categories: [生醫文章]
tags: [Biomedicine,bioinformatics]
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
1. 先用 bulk RNA-seq（+ rMATS）找「改變的剪接事件」與 ΔPSI，同時觀察到 `ESRP2 這個 RBP 在疾病中下調`。
2. 接著做 ESRP2 的 eCLIP，用 UV 交聯＋免疫沉澱把 ESRP2 當下「黏住的 RNA 片段」抓出來並定序，`畫出 ESRP2 的結合位點地圖`。
3. 再把 eCLIP 的結合峰 與 rMATS 找到的可變外顯子（ΔPSI） `做重疊`，若峰值富集在外顯子或剪接位點附近，就支持「ESRP2 直接調控這些錯剪事件」。
4. 同步用 Exon Ontology 解讀這些外顯子是否帶有 NLS/功能域/PTM 位點 等功能訊息，並做實驗驗證（例如誘導外顯子跳躍造成蛋白核→質轉位）。

> 「顯著可變外顯子（ΔPSI）」指的是：在兩組條件（例如疾病 vs 對照）之間，某個可變剪接事件的外顯子納入比例（PSI, Percent Spliced In）發生了具有統計意義的改變。PSI 近似可寫為：PSI =（支持「外顯子被納入」的接點讀數）/（納入讀數 + 跳過讀數）；而 ΔPSI = PSI_案例 − PSI_對照，因此 ΔPSI > 0 表示該外顯子在案例更常被納入，ΔPSI < 0 則更常被跳過。常見用 rMATS 等工具，對各類事件（SE：外顯子跳躍、RI：內含子保留、A5SS/A3SS：5'/3' 端可變剪接、MXE：互斥外顯子）估計 PSI，並以多重校正後的 FDR 門檻（如 FDR < 0.05 或 0.1）、最小接點讀數（Junction read out, 如 ≥10）及 |ΔPSI| 門檻（如 ≥0.1，即 10% 變化）來定義「Differential splicing」。在這篇文脈中，先用 ΔPSI 找出「真的剪接有變」的外顯子，再用 Exon Ontology 判斷這些外顯子是否包含功能關鍵元素（如 NLS、功能域、PTM 位點），最後再用 eCLIP 檢查調控該事件的 RBP 是否在該外顯子附近有直接結合證據。