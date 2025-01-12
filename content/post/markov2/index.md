---
title: 計算生物學聊聊：Hidden Markov Chain (下)
date: 2025-01-12
authors: ["戴揚紘", ""]
commentable: true
categories: [計算生物學]
tags: [Computational biology,data science]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在上一章節，我們介紹了 Hidden Markov Model（HMM）的基本架構與 Forward Algorithm。本篇將進一步探討其他常見的 HMM 演算法，包括 Backward Algorithm、Forward-Backward Algorithm，以及解碼問題中的 Viterbi Algorithm，並說明其數學基礎及應用。

---
## Backward Algorithm

Backward Algorithm 是 Forward Algorithm 的「對偶」，用於計算從時間點 $t$ 開始到序列結束生成觀察序列的機率。它主要用於與 Forward Algorithm 結合，進行參數估計和隱藏狀態的後驗分佈計算。

1. 初始化(時間 $t = T$)：
$$
\beta_T(i) = 1, \quad \text{for } 1 \leq i \leq N
$$

i 表示不同的隱藏狀態， 表示在最後一個時間點的`機率總和為 1`，意即後面不會再有觀測值，機率已確定。

2. 遞推(時間 $t < T$)：

$$
\beta_t(i) = \sum_{j=1}^N a_{ij} \cdot b_j(o_{t+1}) \cdot \beta_{t+1}(j), \quad 1 \leq i \leq N
$$

其中：
- $\beta_t(i)$ 是在狀態 $s_i$ 且從時間點 $t+1$ 到序列結尾的觀察機率。
- $a_{ij}$ 是狀態 $s_i$ 到 $s_j$ 的轉移機率。
- $b_j(o_{t+1})$ 是狀態 $s_j$ 生成觀察值 $o_{t+1}$ 的機率。

其實就是forward algorithm 的計算方式由後往前算，因為每一個機率節點已經`繼承`了前一個或後一個節點傳輸過來的資訊，因此可以接續往下計算。前向算法與後向算法的差別在於，一個機率取決於已經出現的觀察值，一個取決於未來值，即某一個時間點的前與後面的序列。

此外，最重要的結論是不管前向還是後向，對總觀察機率的計算結果是一致的，因為總序列相同，條件的參數也相同。

---
## Forward-Backward Algorithm
前面講的forward algorithm 或是 backward algorithm 是用在觀測值機率的計算，但是如果要計算隱藏態的機率，就必須要靠兩者的結合。而隱藏狀態也是條件機率，但是前向和後向給的條件不同，也就是序列不同，所以兩者所評估的隱藏狀態分不會不一樣，因此必須要結合兩者來正確評估隱藏狀態的分佈。
Forward-Backward Algorithm 結合 Forward 和 Backward 的結果，用於計算隱藏狀態的後驗分佈（Posterior Distribution）。這在參數重估（如 Baum-Welch Algorithm）或狀態分析中非常重要。

### 後驗機率計算公式
給定觀察序列 $O = \{o_1, o_2, \dots, o_T\}$，隱藏狀態 $s_i$ 在時間 $t$ 出現的後驗機率為：

$$
P(s_t = i \mid O, \lambda) = \frac{\alpha_t(i) \cdot \beta_t(i)}{P(O \mid \lambda)}
$$

其中：
- $\alpha_t(i)$ 是 Forward Algorithm 在時間 $t$ 的結果。
- $\beta_t(i)$ 是 Backward Algorithm 在時間 $t$ 的結果。
- $P(O \mid \lambda)$ 是觀察序列的總機率，可用 Forward 或 Backward 計算：

$$
P(O \mid \lambda) = \sum_{i=1}^N \alpha_T(i)
$$

---
## Viterbi Algorithm
Viterbi Algorithm 用於解碼問題，即在給定觀察序列的情況下，找出最可能的隱藏狀態序列（最短路徑問題）。

### 數學公式

1. 初始化(時間 $t=1$)：

$$
\delta_1(i) = \pi_i \cdot b_i(o_1), \quad \psi_1(i) = 0, \quad 1 \leq i \leq N
$$

- $\delta_1(i)$ 表示狀態 $s_i$ 在時間 $t=1$ 的最優路徑機，也就是`機率較大`的那條。
- $\psi_1(i)$ 是回溯指標，用於記錄上一個狀態。

1. 遞推(時間 $t > 1$)：

$$
\delta_t(i) = \max_{j=1}^N \big[\delta_{t-1}(j) \cdot a_{ji}\big] \cdot b_i(o_t), \quad 1 \leq i \leq N
$$

$$
\psi_t(i) = \arg\max_{j=1}^N \big[\delta_{t-1}(j) \cdot a_{ji}\big]
$$

- $\delta_t(i)$ 是到時間 $t$ 並到達狀態 $s_i$ 的最優路徑機率。
- $\psi_t(i)$ 是到達 $s_i$ 的最可能上一個狀態。

3. 回溯：

從最後一個時間點 $T$ 開始，找到最可能的終點狀態：

$$
s_T^* = \arg\max_{i=1}^N \delta_T(i)
$$

然後根據 $\psi$ 回溯最優隱藏狀態序列：

$$
s_t^* = \psi_{t+1}(s_{t+1}^*), \quad t = T-1, T-2, \dots, 1
$$

和forward-backward 演算法相比，Viterbi 在多數情況下會給出相似的計算，但因為Viterbi只會考慮最優解，所以會忽略其他路徑的貢獻，但forward-backward 演算法可能會給出機率較低的隱藏態。Forward-Backward 的後驗概率分佈反映了所有可能隱藏狀態的加權機率，而不是選擇單一路徑。因此，對某些時間點，它可能偏向於總體解釋力強但機率較低的狀態。

## 其他演算法：Baum Welch Algorithm
Baum-Welch 演算法是一種基於 EM (Expectation-Maximization) 框架的HMM參數學習方法，通過 Forward-Backward 演算法計算隱藏狀態的後驗分佈，並迭代更新初始分佈、轉移機率和觀察機率，以最大化觀察序列的對數似然值。其精髓在於將不可觀測的隱藏狀態以概率分佈的形式處理（軟標籤），適用於無監督學習的序列數據建模，但可能受初始值影響，易陷入局部最優。

---
## 總結
本篇主要介紹了 HMM 的三個核心演算法：Backward Algorithm、Forward-Backward Algorithm 和 Viterbi Algorithm。這些演算法在生物資訊學中被廣泛應用，例如基因組注釋、蛋白質結構預測和序列比對。未來的篇章將繼續探討這些演算法的實際應用案例。
