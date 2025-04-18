---
title: 單細胞RNA-seq數據分析教學-4：整合單細胞數據集
date: 2025-04-14
authors: ["戴揚紘", ""]
commentable: true
categories: [單細胞定序]
tags: [基因體學,生物資訊學]
isCJKLanguage: true
draft: true
---
<!--more-->
## Quick look





步驟5：進階應用拓展

在完成基本整合與下游分析後，研究者可根據資料特性與研究目標進行更進階的分析，例如細胞類型註解、跨模態整合（如scATAC-seq）、空間轉錄體對齊等。以下將針對幾個熱門應用進行說明。

5.1 細胞類型自動註解（Automatic Cell Type Annotation）

透過已知標記資料集，可利用監督式比對方法為未知樣本進行自動標註。

SingleR（使用參考表達譜進行比對）

library(SingleR)
ref <- celldex::HumanPrimaryCellAtlasData()
pred <- SingleR(test = GetAssayData(seurat, slot = "data"), ref = ref, labels = ref$label.main)
seurat$SingleR_label <- pred$labels
DimPlot(seurat, group.by = "SingleR_label")

scmap（基於最近鄰的向量投影方法）

library(scmap)
library(SingleCellExperiment)
sce <- as.SingleCellExperiment(seurat)
sce <- selectFeatures(sce)
sce <- indexCluster(sce)
sce_query <- sce  # 可替換為另一資料集
sce_query <- scmapCluster(projection = sce_query, index_list = list(ref = metadata(sce)$scmap_cluster_index))
colData(sce_query)$scmap <- sce_query$scmap_cluster_labs

5.2 跨模態整合：scRNA-seq 與 scATAC-seq 整合

Seurat v4 支援多模態分析，可將scRNA-seq與scATAC-seq資料進行整合與對齊。

整合步驟概要：

使用Signac處理ATAC資料

使用FindTransferAnchors()尋找跨模態anchor

使用TransferData()進行資料投影與標註轉移

library(Signac)
# 建立RNA與ATAC Seurat物件後：
transfer.anchors <- FindTransferAnchors(reference = seurat_rna, query = seurat_atac, reduction = "cca")
predicted.labels <- TransferData(anchorset = transfer.anchors, refdata = seurat_rna$celltype, weight.reduction = seurat_atac["lsi"])
seurat_atac$predicted_celltype <- predicted.labels$predicted.id

5.3 空間轉錄體整合（Spatial Transcriptomics Integration）

若有空間資料（如10x Visium），可利用整合技術將scRNA-seq細胞類型或表現投影至空間位置。

Seurat範例：

# spatial_obj: Visium Seurat物件；seurat_rna: scRNA-seq物件
anchors <- FindTransferAnchors(reference = seurat_rna, query = spatial_obj, normalization.method = "SCT")
predictions <- TransferData(anchorset = anchors, refdata = seurat_rna$celltype, weight.reduction = spatial_obj["pca"])
spatial_obj$predicted_celltype <- predictions$predicted.id
SpatialDimPlot(spatial_obj, group.by = "predicted_celltype")

補充工具資源與建議

celldex：提供多種公開註解參考資料庫供SingleR使用

scmap：支援快速比對與高可擴展性的細胞標註方法

Signac：處理scATAC-seq與整合分析的Seurat附加模組

SeuratData：提供教學用的整合資料集（如PBMC, COVID lung）

最終總結

本課程不僅介紹了四種常見的scRNA-seq整合工具，還涵蓋整合品質評估、常見下游分析，並拓展至進階應用如細胞類型自動註解、scATAC-seq整合與空間轉錄體對齊。透過這套流程，研究者可對複雜的單細胞資料集進行全面整合與深入解讀，實現更具系統性的生物學發現。

