---
title: 單細胞RNA-seq數據分析教學-2：從數據處理到降維視覺化
date: 2025-03-16
authors: ["戴揚紘", ""]
commentable: true
categories: [單細胞定序]
tags: [基因體學,生物資訊學]
isCJKLanguage: true
draft: true
---
<!--more-->
## Quick look








---





## 細胞群聚





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




