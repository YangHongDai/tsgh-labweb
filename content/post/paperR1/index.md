---
title: 黑色素瘤如何對免疫治療產生抗藥性？
date: 2024-11-23
authors: ["戴揚紘", ""]
commentable: true
---
<!--more-->
## Quick look 
這篇[文章](https://www.nature.com/articles/s41467-023-36979-y)研究了Immune checkpoint inhibitor（ICI）療法在黑色素瘤中(melanoma)的抗藥性機制。通過分析來自患者的短期腫瘤細胞系(short term cell line))和匹配的腫瘤樣本，作者發現了三種不同的抗藥性機制，分別涉及抗原表達的喪失、抗原呈現的破壞，以及與PTEN缺失相關的免疫細胞排斥。這些抗藥性機制揭示了可能的救援性治療策略，例如恢復MHC的表達、促進先天免疫反應、以及重新激活野生型抗原表達。
# 簡介
免疫檢查點抑制劑（ICI）針對PD-1的療法已徹底改變了轉移性黑色素瘤患者的治療方式。在III期臨床試驗中（如CheckMate-067和KEYNOTE-006），PD-1抑制劑顯示了42-45%的客觀反應率，以及6.5年42%的總體生存率。然而，約有55%的黑色素瘤患者對單獨的PD-1抑制劑療法存在先天性抗藥性，並且幾乎25%的患者在治療初期有反應，但在兩年內產生了抗藥性。因此，抗藥性問題仍然是ICI療法的一個重大挑戰。本研究通過全面分析黑色素瘤中對免疫檢查點抑制劑的抗藥性機制，試圖理解這些阻礙ICI療法療效的因素。

為此，研究人員利用短期腫瘤細胞系和匹配的腫瘤樣本，通過基因組、轉錄組和高維流式細胞術的分析方法，揭示了抗藥性形成的分子和功能特徵。他們總結出了三個主要的抗藥性機制：抗原表達喪失、抗原呈遞破壞和免疫細胞排斥，這些機制可能為治療提供新的思路和目標。

# 研究結果
## 抗原表達消失了？
研究發現，腫瘤細胞內源性的<span style="color: red; font-weight: bold">IFNγ(干擾素γ</span>)號是導致黑色素瘤去分化的重要因素之一，這種去分化的過程使腫瘤細胞喪失了野生型抗原的表達能力，從而減少了腫瘤細胞的免疫原性。IFNγ信號在黑色素瘤細胞內部的作用過程中，干擾了腫瘤細胞的抗原呈遞功能，進而導致了抗原喪失。此外，該研究還觀察到，一些患者腫瘤中<span style="color: red; font-weight: bold">JAK2</span>基因的缺失或突變，使得IFNγ訊息路徑被中斷，進一步影響了MHC-I（主要組織相容性複合體I類）和MHC-II的表達，從而使腫瘤細胞更難被免疫系統辨識。

JAK2的缺失影響到MHC-I和MHC-II分子的表達，這是因為JAK2在IFNγ信號中負責<span style="color: red; font-weight: bold">STAT1(信號轉導和轉錄活化因子1)</span>（的磷酸化，進而驅動MHC的表達。JAK2缺失導致了STAT1無法被激活，使MHC的表達無法啟動，從而削弱了腫瘤對免疫系統的可見性(visibility)。在這些細胞系中，即使使用外源性的IFNγ進行處理，依然無法恢復MHC表達，顯示出這一抗藥性是基因缺失所導致的不可逆過程。

## 抗原呈現遭到抑制？
除了抗原表達的喪失外，研究還發現了一系列影響抗原呈現的獨立機制，這些機制也會導致免疫檢查點抑制劑的抗藥性。其中一個重要的機制是<span style="color: red; font-weight: bold">B2M</span>基因的功能喪失突變。B2M是MHC-I複合體的重要組成部分，當B2M基因出現突變時，MHC-I的組裝和細胞表面表達均會受到影響，從而降低腫瘤細胞被T細胞識別的可能性。

此外，<span style="color: red; font-weight: bold">CIITA(MHC-II轉錄調控因子)</span>基因的表達沉默也是一個關鍵因素。CIITA是控制MHC-II表達的核心轉錄因子，當該基因被表觀遺傳機制（如DNA甲基化或組蛋白去乙醯化）抑制時，MHC-II的表達將顯著降低，進而影響抗原呈現。研究中通過表觀遺傳抑制劑（如HDAC抑制劑）恢復CIITA的表達，結果顯示MHC-II的表達可以部分恢復，這表明表觀遺傳調控在抗原呈遞中的重要性。

## 免疫細胞排斥？
<span style="color: red; font-weight: bold">PTEN</span>基因的缺失與腫瘤中的免疫細胞排斥有著密切的關聯。PTEN是一個腫瘤抑制基因，其缺失會導致腫瘤細胞分泌更多的免疫抑制性分子，如TGF-β等，從而阻礙免疫細胞（尤其是CD8+ T細胞）進入腫瘤微環境。在研究中，PTEN缺失的黑色素瘤顯示出更低的CD8+ T細胞浸潤，並且在腫瘤微環境中存在更高比例的巨噬細胞，這些巨噬細胞通常具有免疫抑制的功能，進一步降低了腫瘤對免疫治療的反應。

PTEN缺失的黑色素瘤還與腦轉移有關。研究發現，腦轉移腫瘤中PTEN缺失的比例較高，這些腫瘤不僅缺乏CD8+ T細胞的浸潤，還顯示出較高的調節性T細胞（Tregs）和巨噬細胞含量，這些免疫細胞的存在進一步加劇了腫瘤的免疫抑制狀態，使ICI療法難以奏效。

# 探討
本研究結果顯示，黑色素瘤對免疫檢查點抑制劑的抗藥性主要涉及三大方面：抗原表達的喪失、抗原呈現的破壞以及免疫細胞排斥。抗原表達喪失與腫瘤細胞的去分化和內源性的IFNγ訊號有關，這些機制共同降低了腫瘤細胞的免疫抗原性，並使其難以被T細胞識別。抗原呈現的破壞則主要涉及MHC-I和MHC-II的異常，這些異常通常由基因突變或表觀遺傳調控引起。而PTEN的缺失則通過影響腫瘤微環境，抑制了免疫細胞的浸潤和活性，進一步促進了腫瘤的免疫逃逸。

根據這些發現，研究者提出了一些潛在的治療救援策略。例如，對於抗原呈現異常的腫瘤，可以通過表觀遺傳調控劑（如HDAC抑制劑）恢復MHC表達，從而增強免疫系統對腫瘤的識別。此外，對於因PTEN缺失而造成免疫細胞排斥的腫瘤，可以考慮使用激活先天免疫系統的療法，如Toll樣受體激動劑，來增強腫瘤微環境中的免疫活性。

去分化的黑色素瘤則更具挑戰性，因為這些腫瘤通常表現出較高的抗藥性和免疫逃逸能力。研究者建議，結合免疫療法與促進鐵依賴性氧化壓力的藥物（如鐵死亡誘導劑），可能有助於改善免疫檢查點抑制劑的療效。此外，針對腫瘤微環境中的免疫抑制因素，如Tregs和免疫抑制性巨噬細胞，也應該考慮相應的干預措施，以減少這些細胞對抗腫瘤免疫反應的負面影響。

這項研究為理解黑色素瘤的免疫檢查點抑制劑抗藥性提供了重要的分子和功能線索，並為未來的治療策略提供了方向。通過精準識別不同的抗藥性機制，並針對性地進行治療，我們有望改善黑色素瘤患者的治療效果，特別是對於那些對現有免疫療法無反應的患者。這些新策略的探索與應用，將可能為免疫治療的挽救治療開創新的局面。




