---
title: 會議探討-The awesome power of genetic linkage
date: 2025-09-15
authors: ["戴揚紘", ""]
commentable: true
categories: [會議探討]
tags: [Biomedicine,bioinformatics]
isCJKLanguage: true
draft: true
---
<!--more-->
## 會議標題
禿頭
2005 年找到Androgen receptor 與禿頭有關，且位在X chromosomee 但不知道在哪裡
找了95 家族，genotyping 許多位在X chromosome 上的基因，把可能性限縮到P arm，當然這都是在GWAS 時代之前的事

## 孟德爾的豌豆


## Violation of independent assortment
1) 為什麼會「違反 9:3:3:1」？——Bateson & Punnett 的甜豌豆（1905–1908）
孟德爾的第二定律（獨立分配）預期雙性狀雜交的 F₂ 比例是 9:3:3:1。但 William Bateson 與 Reginald Punnett 在甜豌豆做雙性狀雜交（花色：紫/紅；花粉形狀：長/圓）時，發現子代表型配對「過度一起出現」或「過度分開」，偏離 9:3:3:1。他們提出「耦合（coupling）／排斥（repulsion）」來描述這種同向或相斥的遺傳趨勢；事後才被我們理解為位於同一染色體上的基因會一起傳遞（連鎖），只有在發生**互換（crossing over）**時才被打散。這組實驗是對「獨立分配」最早、最清楚的例外證據之一。

2) 從「例外」到「理論」——Morgan 的連鎖群與性連鎖（1910–1911）
在果蠅研究中，Thomas H. Morgan 以白眼等性狀證明基因位在染色體上，而且同一條染色體上的基因會形成「連鎖群」，不再滿足完全獨立分配；這為「連鎖」提供了體系性的概念框架，也鋪路給後續的測圖工作。
Nature
3) 怎麼量「基因距離」？——Sturtevant 的第一張遺傳圖（1913）
Morgan 的學生 Alfred H. Sturtevant 靈光一現：互換頻率與兩基因在染色體上的距離近似成正比，於是在 1913 年用果蠅資料畫出了世界第一張遺傳連鎖圖，建立了以 1% 重組率 = 1 centiMorgan (cM) 的測距單位與線性排列概念，這讓「連鎖」從現象學躍升為可量化的地圖學。

4) 「互換」真的有物理對應嗎？——玉米第 9 染色體的直接證據（1931）
連鎖與互換若為真，基因型的重組應伴隨染色體片段的交換。Harriet Creighton 與 Barbara McClintock 在玉米（Zea mays）第 9 號染色體上，利用一對可在顯微鏡下辨識的**「旋節（knob）」與易位標記**，同時追蹤鄰近基因（如 C、Wx 等）的重組：他們發現表型重組與染色體片段物理互換同時發生，首次把「遺傳重組」與「染色體物理交換」一一對上，成為經典的連鎖/互換的細胞學證據。同年 Curt Stern 在果蠅也以體細胞嵌合現象補上了平行證據。

什麼是家族型連鎖分析 (family-based linkage analysis)
定義
一種利用 家族資料 來找尋遺傳疾病相關基因的方法。
原理是：如果某段 DNA 與疾病表現型在家族成員中一同遺傳 (co-segregate)，就表示該區域可能含有致病基因。
🔬 核心概念
基因座相鄰 → 連鎖 (linkage)
基因位在同一染色體上、距離近時，不容易被減數分裂時的重組 (recombination) 打斷。
因此會一起傳遞到下一代。
用標記 (genetic markers) 追蹤
透過微衛星 (microsatellite) 或 SNP 標記來觀察家族中哪些 DNA 片段與疾病狀態「一起遺傳」。
LOD score (對數似然比)
連鎖分析的統計方法，LOD ≥ 3 通常被認為有顯著連鎖證據。
🧪 實際做法
收集一個或多個 受影響的家族（患病與未患病成員）。
建立 家系圖 (pedigree)，並採集基因型資料。
假設一個遺傳模式（常染色體顯性 / 隱性、X 聯鎖等）。
計算標記與疾病基因的重組率 (θ)。
用 LOD score 判斷標記是否與疾病位點連鎖。
💡 舉例
假設有家族：
祖父母 → 爸媽 → 孩子
觀察到某個 microsatellite 標記 每次只要小孩患病，必定帶有標記 A，而沒病的小孩從不帶 A。
這就表示：疾病基因很可能跟這個標記「靠得很近」，因為它們 隨著減數分裂一起被遺傳下來。
這時候研究者會：
找到這個區域（可能幾 Mb 大）
再進一步做 精細定位、候選基因測序 → 才能真正找出致病基因。
早期找出 囊性纖維化 (CFTR)、亨丁頓舞蹈症 (HTT)、BRCA1/2 乳癌基因 都是靠 family-based linkage analysis。
研究者追蹤多代家族，發現某些 DNA 標記總是與疾病共同遺傳 → 鎖定基因位置 → 再進一步精細定位與功能研究。
📊 優缺點
✅ 優點
對於 高度遺傳性、單基因疾病 特別有效。
能在沒有大規模群體資料的情況下找到候選基因區域。
⚠️ 限制
需要大型多代家族資料。
對多基因或複雜疾病（例如糖尿病、心血管疾病）效果差。
精度有限（通常定位到數百 kb ~ 數 Mb 區間）。

Family based linkage analysis
successful for human mendelian triats but limited for complex traits 
High confidence: genotype --> phenotype (high penetrance, highg effect size)
Low confidence for complex traits 