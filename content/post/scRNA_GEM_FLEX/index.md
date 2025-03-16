---
title: 單細胞RNA-seq數據分析教學-1：從數據處理到細胞註解
date: 2025-03-16
authors: ["戴揚紘", ""]
commentable: true
categories: [單細胞定序]
tags: [基因體學,生物資訊學]
isCJKLanguage: true
draft: true
---

## 安裝與導入必要套件
```r
# 基礎分析套件
install.packages("Seurat")
install.packages("dplyr")
install.packages("patchwork")
install.packages("ggplot2")

# 輔助套件（用於快速標記基因分析）
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("presto")  # 快速Wilcoxon檢定

# 加載套件
library(Seurat)
library(dplyr)
library(patchwork)
library(presto)
```
## 創建Seurat物件
從10x Genomics數據讀取並構建Seurat物件：
```r
# 讀取10x數據
counts <- Read10X(data.dir = "scRNA_data/scRNA_project1")
seurat <- CreateSeuratObject(counts, project = "scRNA_project1")

# 手動讀取非10x數據（例如矩陣文件）
counts <- readMM("scRNA_data/scRNA_project1/matrix.mtx.gz")
features <- read.csv("scRNA_data/scRNA_project1/features.tsv.gz", sep = "\t", header = FALSE)
colnames(counts) <- readLines("scRNA_data/scRNA_project1/barcodes.tsv.gz")
rownames(counts) <- make.unique(features[,2])
seurat <- CreateSeuratObject(counts, project = "scRNA_project1")
```
關於讀取要使用的函式，如果資料夾裡面是以下文件，使用`Read10X()`
- `matrix.mtx.gz` (稀疏矩陣格式的基因表達數據)
- `features.tsv.gz` (基因名稱與編號)
- `barcodes.tsv.gz` (細胞條碼資訊) 通常只有一行，所以很適合用`readLines`來逐列讀取，存成`character`向量。
這些檔案通常是 gzip 壓縮格式（.gz），但 Read10X() 也可以讀取未壓縮的版本（即 .mtx、.tsv）。

如果資料夾裡的檔案是CellRanger 處理好的輸出: filtered_feature_bc_matrix.h5，使用`Read10X_h5()`

## 品質控制（QC）
這一步我們希望過濾掉：
1. 偵測到太少基因的細胞：常見原因是測序深度太淺，通常研究需要2-2.5倍的測序深度 (1倍為10000 reads per cell)。
2. 偵測到太多基因的細胞：可能原因為一顆油滴包到兩顆以上的細胞 (doublet or multiplet)，所以共享cell barcode，導致基因數量大增。
3. 太多粒線體的轉錄本：大多的scRNA-seq實驗是用oligo-T去抓mRNA，理論上不會抓到粒線體的基因，因為粒線體RNA缺少poly-A tail，但難免會抓到一些。也有證據顯示一些粒線體的轉錄本帶有poly-A tails作為降解的標記。原則上，太多粒線體基因表示細胞處於stress （如缺氧），所以產生更多粒線體。

而Seurat可以基於以下指標，過濾低質量細胞：
- `nFeature_RNA`：每個細胞檢測到的基因數
- `nCount_RNA`：總轉錄本數
- `percent.mt`：粒線體基因比例

針對粒線體基因比例需要手動設定：
```r
# 計算線粒體基因比例
seurat[["percent.mt"]] <- PercentageFeatureSet(seurat, pattern = "^MT-")
```

請注意，針對需要過濾的基因數量，並不存在one-size fits all的過濾條件，所以建議過濾掉outlier cells 即可，也就是明顯不屬於大部分細胞的細胞群。因此我們可以先視覺化基因分佈圖：
```r
# 可視化QC指標
VlnPlot(seurat, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)

# 過濾細胞（根據分佈調整閾值）
seurat <- subset(seurat, subset = 
    nFeature_RNA > 500 & 
    nFeature_RNA < 5000 & 
    percent.mt < 5 
)
```


## 數據標準化與特徵選擇
XXX


```r
# 標準化（LogNormalize）
seurat <- NormalizeData(seurat)

# 識別高度可變基因（HVGs）
seurat <- FindVariableFeatures(seurat, nfeatures = 3000) #可以2000-3000視情況而定

# 可視化HVGs
top20 <- head(VariableFeatures(seurat), 20)
plot <- VariableFeaturePlot(seurat)
LabelPoints(plot, points = top20, repel = TRUE)
```

##  數據縮放與降維

SCTransform
```r
# 縮放數據（可選回歸變異源）
seurat <- ScaleData(seurat, vars.to.regress = c("nFeature_RNA", "percent.mt"))

# PCA降維
seurat <- RunPCA(seurat, npcs = 50)

# 可視化PCA結果（肘部圖）
ElbowPlot(seurat, ndims = 50)

# 選擇前20個主成分進行後續分析
```





## 非線性降維與分群
scRNA-seq分析通常基於多個基因的表達值來比較細胞。例如，聚類分析 (clustering) 透過計算細胞在多個基因上的歐幾里得距離，來識別具有相似轉錄組特徵的細胞。在這些應用中，每個基因都可以視為一個數據維度。舉個簡單的例子，假設我們的數據集中僅包含兩個基因，那麼我們可以用二維圖來表示，每個軸對應一個基因的表達量，而圖上的每個點代表一個細胞。當數據集包含數千個基因時，每個細胞的表達譜就構成了一個高維表達空間中的位置。

降維 (dimensionality reduction) 的目標是減少數據的維度數量，以便進行更高效的分析。
這是因為許多基因的表達是相關的，受到相同的生物過程影響，因此無需單獨存儲每個基因的資訊，而是可以將多個基因的特徵壓縮到少數幾個統合的維度，例如`特徵基因 (eigengene)`（Langfelder 和 Horvath，2007）。降維的主要優勢包括：

- 減少計算負擔，使後續如聚類等分析僅需在少數維度上運算，而非上千個基因。
- 降低數據噪聲，透過整合多個基因的資訊來獲得更穩定的模式表現。
- 便於數據可視化，讓我們能夠在 2D 或 3D 圖 中直觀展示細胞間的關係，避免高維度的數據難以理解的問題。

而且降維後，會將稀疏矩陣轉換成較緊密的數據(compact)，有助於後續的分析的效率與可靠性。這種方式對分析基本上沒有缺點，除非是整合百萬細胞數量等級的數據，可能需要保存稀疏矩陣的特性來減少記憶體的佔用 (可以用`truncated SVD` 或是 `autoencoder`)。

透過降維技術，如主成分分析 (PCA) 和 t-SNE、UMAP 等非線性方法，研究者可以更有效地探索單細胞數據的內在結構，發現潛在的細胞類型與功能模式。


```r
# UMAP降維
seurat <- RunUMAP(seurat, dims = 1:20) # UMAP 資訊會自動存在seurat裡更新

# 分群（分辨率決定分群細緻度）
seurat <- FindNeighbors(seurat, dims = 1:20)
seurat <- FindClusters(seurat, resolution = 0.8)

# 可視化分群結果
DimPlot(seurat, reduction = "umap", label = TRUE)
```

## 細胞註解（Cell Annotation）
基於已知標記基因或參考數據集進行註解。

方法1：手動標記基因檢查
```r
# 定義標記基因列表
markers <- c("SOX2", "NES", "DCX", "FOXG1", "EMX1", "DLX2", "GAD1")

# 可視化標記基因表達
FeaturePlot(seurat, features = markers, ncol = 3)
VlnPlot(seurat, features = markers, pt.size = 0)

# 根據表達模式標註分群
new.cluster.ids <- c(
    "0" = "Neural Progenitors",
    "1" = "Neurons",
    "2" = "Glutamatergic Neurons",
    "3" = "GABAergic Neurons"
)
seurat <- RenameIdents(seurat, new.cluster.ids)
DimPlot(seurat, label = TRUE)
```

## 方法2：自動化註解工具
#### Garnett：基於機器學習的註解工具
```r
# 安裝與使用
BiocManager::install("garnett")
library(garnett)
# 需準備訓練好的分類器（參考官方文檔）
```

#### SingleR：對比參考數據集
```r
# 安裝
BiocManager::install("SingleR")

# 使用示例
library(SingleR)
ref <- celldex::HumanPrimaryCellAtlasData()
pred <- SingleR(test = seurat@assays$RNA@data, ref = ref, labels = ref$label.main)
seurat$SingleR_labels <- pred$labels
DimPlot(seurat, group.by = "SingleR_labels")
```
## 方法3：參考數據集整合（Seurat v4+）
```r
# 假設已加載參考數據集seurat_ref
anchors <- FindTransferAnchors(
    reference = seurat_ref,
    query = seurat,
    dims = 1:30
)
predictions <- TransferData(
    anchorset = anchors,
    refdata = seurat_ref$cell_type
)
seurat$predicted_labels <- predictions$predicted.id
DimPlot(seurat, group.by = "predicted_labels")
```
## 推薦輔助套件
#### presto：快速差異基因分析
```r
# 安裝
remotes::install_github("immunogenomics/presto")

# 使用
markers <- wilcoxauc(seurat, group_by = "seurat_clusters")
top_markers <- markers %>% group_by(group) %>% top_n(10, auc)
```
#### voxhunt：對比Allen Brain Atlas
```r
# 安裝
devtools::install_github("quadbiolab/voxhunt")

# 使用
library(voxhunt)
load_aba_data('path_to_ABA_data')
vox_map <- voxel_map(seurat, genes_use = VariableFeatures(seurat))
plot_map(vox_map)
```
#### scCATCH：自動細胞註解
```r
# 安裝
remotes::install_github("ZJUFanLab/scCATCH")

# 使用
library(scCATCH)
clusters <- seurat@active.ident
markers <- find_markers(seurat, clusters)
celltype <- scCATCH(markers, species = "Human", tissue = "Brain")
```
---
## 常見問題與解決方案
套件安裝錯誤：確保R與Bioconductor版本兼容，或從GitHub直接安裝開發版。
記憶體不足：使用subset縮減數據規模，或轉換為稀疏矩陣。
註解不準確：結合多種方法（如手動檢查與自動化工具）交叉驗證。
透過以上步驟，可完成從數據預處理到細胞註解的全流程分析。建議根據實際數據特性調整參數（如分群分辨率、標記基因列表），並參考套件官方文檔以獲得最佳結果。




