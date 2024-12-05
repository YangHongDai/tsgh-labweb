---
title: 纖維母性網狀細胞為肺癌中的T細胞塑造碉堡？
date: 2024-11-27
authors: ["戴揚紘", ""]
commentable: true
categories: [免疫治療]
tags: [Immunotherapy, lung cancer, T cell]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look 
腫瘤內部的免疫微環境基本上都存在高度異質性，從免疫細胞密集分布到完全缺乏等等。目前的證據顯示，腫瘤抗原特異性T細胞(Tumor-specific T cell)若要順利的啟動及維持他們的活性，仰賴腫瘤引流淋巴結(tumor draining lymph node)和腫瘤組織內的微環境，特別是三級淋巴結構（tertiary lymphoid structure，TLS），其通常位於腫瘤邊緣並由B細胞主導。而TLS中的B細胞活性也與Immune checkpoint inhibitor的成功率息息相關。

這些免疫細胞由專門的纖維母細胞(如T細胞區網狀細胞和血管周圍網狀細胞)支撐，而這之間的交互作用也從TLS透過某種物理架構延伸到腫瘤內部。本篇研究通過單細胞轉錄組學和高解析度顯微技術，發現了在肺癌中形成特定T細胞環境的纖維母細胞亞群(fibroblastic reticular cell)。這些FRC與免疫細胞的互動促進了TLS的形成、T細胞軌跡中的分化，以及控制T細胞活性。實驗顯示，破壞腫瘤微環境中FRC與免疫細胞的互動會降低CD8+ T細胞的抗腫瘤活性並促進腫瘤生長。

由此可見，特定的FRC亞群通過提供增長和分化的信號，在腫瘤內部支持保護性免疫反應(protective immunity)，對抗腫瘤生長。

# FRC細胞與肺癌腫瘤內部T細胞關係不尋常？
對肺癌來說，有肋膜侵犯是一項不好的預後因子，而研究也發現，由subpleural region(Subpleural margin, SM，有肋膜侵犯的部分)切下的腫瘤，與位於central(central margin, CM，同一塊腫瘤，靠近中心的部分)的腫瘤在免疫細胞的組成上有顯著個差異。SM腫瘤的淋巴細胞比較鬆散，而且主要位於腫瘤周圍，但CM腫瘤內部有明顯的T細胞浸潤(圖一)。團隊也發現CM腫瘤T細胞附近充滿ACTA2陽性的纖維母細胞，而這些細胞與SM相比，與吸引T細胞有關的chemokine基因CCL19與CCL21之表現亮顯著較高。

![fig1](fig1.png '圖一')

近一步用高解析顯微鏡發現，腫瘤內的T細胞棲息區(niche)，與腫瘤TLS有連結，而CCL19+ FRC更是與T細胞有接觸，而FRC表現的CCL19量的多寡也形成了一條T細胞依循的梯度(gradient)，由此可見CCL19+ FRC似乎主導了腫瘤內T細胞的遷移。

# 探索其中的分子機制
## 精細的交互作用
團隊使用螢光顯微鏡擷取圖片並重組成3D影像，發現在TLS中的CCL19+ POSTN+ PDPN+ 的FRC與T細胞有緊密的接觸，同樣的情形也在CM中血管附近的FRC出現。而利用scRNA-seq分析免疫細胞的interactome也發現，腫瘤內的PRC(perivascular reticular cell)與TRC(T cell zone reticular cell)主要跟CD8+ T細胞作用(圖二)。團隊利用[CellChat](https://www.nature.com/articles/s41467-021-21246-9)分析CCL19+FRC與CD8+T細胞之間的通訊涉及以下信號：
1. 遷移信號：CXCL12和CXCL16。
2. 細胞間的黏附：VCAM1。
3. 激活因子：包括type II interferon。
4. 微環境因子：如LTBR、TNFRSF14和NOTCH3，為CD8+T細胞創造適合的微環境。

總結來說，CCL19+TRCs和PRCs與CD8+T細胞的互動通過一系列信號網絡調節，形成特定的纖維母性微環境，進一步支持T細胞的功能活化和發育。

![fig2](fig2.png '圖二')

## FRC分化路徑
團隊發現除了cancer-associated fibroblast(CAF)會表達CCL19之外，正常肺組織的mural細胞與adventitia細胞也會表現CCL19。因此作者合理懷疑表現CCL19的PRC與TRC來自於血管周圍的纖維母細胞。團隊使用分化路徑分析(differentiation trajectory analysis)後也證實mural細胞會衍生成為PRC；而adventitia細胞會於TRC路徑的根部(圖三)。而團隊進一步使用小鼠肺癌模型(Lewis lung carcinoma expressing the viral glycoprotein peptide 33 of the lymphocytic choriomeningitis virus)也支持這項發現。

![fig3](fig3.png '圖三')

# 小鼠模型也能出現TLS?
根據先前的研究，藉由病毒激活的CD8+T細胞會在發炎組織中形成TLS，因此團隊在小鼠植入肺腫瘤細胞後在第15天接受疫苗注射，此疫苗設計為重組冠狀病毒的質體，可以表現LCMV glycoprotein gp33與myeloid cell stimulating factor Flt3l。在施打疫苗後，腫瘤成功出現腫瘤邊緣與腫瘤內部的TLS，而在小鼠的腫瘤內部的FRC也與CD8+T細胞緊密接觸。

# FRC對CD8+T細胞抗腫瘤的影響？
研究顯示，腫瘤微環境中的FRC在促進抗腫瘤 CD8+ T細胞免疫中發揮關鍵作用。通過使用白喉毒素(DT)去除小鼠Ccl19-Cre+ 細胞，發現FRC的缺失導致腫瘤失去FRC的網絡，顯著減少腫瘤內CD8+ T細胞的募集，並加速腫瘤生長。同時，腫瘤特異性CD8+ T細胞的效應功能(如 IFN-γ、TNF 和 granzyme B 的產生)以及增殖活性(KI67 表達)均顯著下降，且表現出更高的耗竭標誌(如 PD1、TIM3、KLRG1)。FRC 通過粘附分子(如 ICAM1、VCAM1）、趨化因子（CXCL16）和免疫調節細胞因子（如 TGF-β1、TSLP）與CD8+ T 細胞進行交互，促進其細胞毒性、增殖和分化。總結來說，FRC在腫瘤微環境中透過多重免疫調控途徑增強了抗腫瘤免疫反應，其缺失會削弱T細胞功能並促進腫瘤進展。

# 結論
這篇研究揭示，腫瘤微環境中的CCL19表達FRCs在促進抗腫瘤CD8+ T細胞免疫反應中扮演關鍵角色。這些FRCs(包括PRCs和TRCs)形成三維細胞網絡，作為T細胞進入腫瘤實質的“通道”，同時支持T細胞在腫瘤淋巴結(TDLNs)和腫瘤相關淋巴樣結構(TLS)中的活化與擴增。CCL19+ FRCs還維持腫瘤特異性CD8+T細胞的增殖和效應分化，其功能受腫瘤和基質細胞產生的信號調控。這些FRC網絡不僅促進T細胞的遷移，還與患者的良好預後密切相關，未來應致力於探討其他腫瘤類型中FRC的發育途徑，並設計促進PRC/TRC分化的策略，以增強抗腫瘤免疫反應。