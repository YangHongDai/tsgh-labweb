---
title: 生資硬核技術：公開癌症基因數據下載及操作
date: 2024-11-28
authors: ["戴揚紘", ""]
commentable: true
categories: [生物資訊]
tags: [Bioinformatics, data science, cancer, R] 
isCJKLanguage: true
---
<!--more-->
## Quick look
數年前我還是住院醫師的時候是直接在UCSC Xena[平台](https://xenabrowser.net)下載癌症數據，但整個過程很難流程化， 而2019年發表的UCSCXenaTools解決了這個問題，也讓我在前年分析公開數據時方便許多。
UCSCXenaTools是一個專門用來處理UCSC Xena的基因組數據的R套件。該平台集成了多個公開數據庫(如分析癌症數據一定要知道的TCGA、ICGC、TARGET、GTEx等），提供處理過的數據，便於我們進行數據的篩選、連結、探索及下載。UCSCXenaTools的功能強大且操作簡單，在我們先前的[preprint](https://www.biorxiv.org/content/10.1101/2024.07.21.604474v1)發表我也是利用這個套件做TCGA數據的處理，所以這邊就簡單分享我是如何用這個套件來進行分析的。

# 簡介
UCSCXenaTools 通過多個Xena Hubs提供對各類公共基因組數據庫的訪問，這些數據經過規範化處理，支持用戶輕鬆地篩選、探索、下載並應用於進一步分析。目前支持的數據中心包括：

1. UCSC Public Hub
2. TCGA Hub
3. GDC Xena Hub
4. ICGC Xena Hub
5. Pan-Cancer Atlas Hub
6. Toil RNAseq Hub 等。
我們可以通過函數如 XenaGenerate()、XenaFilter() 等組合進行操作，並結合其他R套件(如 dplyr)來靈活的處理數據。

# 實際操作流程
詳細的操作流程可以參考發表在STAR Protocols的[這篇](https://star-protocols.cell.com/protocols/1425)，裡面詳細的解釋了每一個步驟以及預期的結果。這邊僅針對基本的操作做介紹:

## 安裝及載入
```r
    install.packages("UCSCXenaTools")
    library(UCSCXenaTools)
```
## 查看可用的所有數據
```r
    #載入XenaData到workspace
    data(XenaData) 
    #查看
    head(XenaData) 
```
這邊輸出的XenaData為一個tibble data frame，包含了所有數據的基本資料，也可以透過這個Xenabrowser的[網址](https://xenabrowser.net/datapages/)來對照。

## 基本操作函數
### 生成數據框: XenaGenerate
```r
    df = XenaGenerate(subset = XenaHostNames == "tcgaHub") %>% 
     XenaFilter(filterDatasets = "clinical") %>% 
     XenaFilter(filterDatasets = "OV") 
```
每一項參數都需要對應到XenaData中的column name

### 搜尋感興趣的數據: XenaScan
```r
    x = XenaScan(pattern = 'Blood') %>%
    XenaGenerate()
```

### 下載數據: XenaQuery
```r
    XenaQuery(df) %>%
    XenaDownload(destdir = 'Data') #記得改路徑

```

## 操作範例
接下來針對大腸癌的資料來舉例:
### 下載TCGA和GTEx數據進行基因表達分析
這邊有一個很重要的概念，根據這篇[論文](https://www.nature.com/articles/s41467-017-01027-z)，Xenabrowser上某癌症類別的數據中，**Solid Tissue Normal**為切除腫瘤附近的健康組織，然而分析時卻發現這類組織的狀態處於真正的健康組織與腫瘤組織之間，所以如果要做差異性基因分析，不要使用下載下來的**Solid Tissue Normal**來當成**Healthy control**，而需要用GTEx上下載的資料來當對照。
```r
# 從 Toil Hub 選擇基因表達數據
    GeneExpectedCnt_toil = XenaGenerate(subset = XenaHostNames == 'toilHub') %>%
    XenaFilter(filterCohorts = 'TCGA TARGET GTEx') %>%
    XenaFilter(filterDatasets = 'TcgaTargetGtex_gene_expected_count')

    XenaQuery(GeneExpectedCnt_toil) %>%
    XenaDownload(destdir = 'Data') #記得改路徑

```
上面的操作直接下載了一個已經經過處理過的合併數據集，包含了TCGA、TARGET以及GTEx的基因資料，而RNA-seq數據已經對hg38基因組做過排序，並用RSEM及Kallisto方法來做[量化](https://www.nature.com/articles/nbt.3772)。

### 下載TCGA臨床數據
```r
    paraCohort = 'TCGA Colon Cancer'
    paraDatasets = 'COAD_clinicalMatrix'

    Clin_TCGA = XenaGenerate(subset = XenaHostNames == 'tcgaHub') %>%
    XenaFilter(filterCohorts = paraCohort) %>%
    XenaFilter(filterDatasets = paraDatasets)

    XenaQuery(Clin_TCGA) %>%
    XenaDownload(destdir = 'Data') #記得改路徑
```
### 下載TCGA存活數據
```r
    Surv_TCGA = XenaGenerate(subset = XenaHostNames == 'toilHub') %>%
    XenaFilter(filterCohorts = 'TCGA TARGET GTEx') %>%
    XenaFilter(filterDatasets = 'TCGA_survival_data')

    XenaQuery(Surv_TCGA) %>%
    XenaDownload(destdir = 'Data') #記得改路徑 
```

### 下載GTEx phenotype數據
```r
    Pheno_GTEx = XenaGenerate(subset = XenaHostNames == 'toilHub') %>%
    XenaFilter(filterCohorts = 'TCGA TARGET GTEx') %>%
    XenaFilter(filterDatasets = 'TCGATargetGTEx_phenotype')

    XenaQuery(Pheno_GTEx) %>%
    XenaDownload(destdir = 'Data') #記得改路徑
```

### 重新處理TCGA與GTEx的樣本名稱
```r
    filterGTEx01 = fread('Data/TcgaTargetGTEX_phenotype.txt')
    names(filterGTEx01) = gsub("\\_", "", names(filterGTEx01)) #將有_的部分去掉

    paraStudy = 'GTEX'
    paraPrimarySiteGTEx = 'Colon'
    paraPrimaryTissueGTEx = '^Colon'

    filterGTEX02 = subset(filterGTEx01,
                      study == paraStudy&
                        primarysite == paraPrimarySiteGTEx &
                        grepl(paraPrimaryTissueGTEx, filterGTEx01$'primary disease or tissue'))

    filterTCGA01 = fread(paste0('Data/',paraDatasets))
    names(filterTCGA01) = gsub("\\_", "", names(filterTCGA01))

    paraSampleType = 'Primary Tumor'
    paraPrimarySiteTCGA = 'Colon'
    paraHistologicalType = 'Colon Adenocarcinoma'

    filterTCGA02 = subset(filterTCGA01,
                      sampletype == paraSampleType&
                        primarysite == paraPrimarySiteTCGA &
                        grepl(paraHistologicalType, filterTCGA01$histologicaltype))
```


### 合併TCGA與GTEx數據
```r
   filterExpr = c(filterGTEX02$sample, filterTCGA02$sampleID, 'sample')
   ExprSubsetBySamp = fread('Data/TcgaTargetGtex_gene_expected_count', select = filterExpr)
```

### 只取protein-coding基因來分析
先從[這裡](https://osf.io/edjzv)下載完整的protein-coding gene資訊。以及在[這邊](https://toil-xena-hub.s3.us-east-1.amazonaws.com/download/probeMap%2Fgencode.v23.annotation.gene.probemap)下載ID/gene mapping。
```r
    probemap = fread('zz_gencode.v23.annotation.csv', select = c(1,2)) #只留前兩欄
    exprALL = merge(probemap, ExprSubsetBySamp, by.x = 'id', by.y = 'sample')
    genesPC = fread('zz_gene.protein.coding.csv')
    exprPC = subset(exprALL, gene %in% genesPC$Gene_Symbol)

    #移除重複基因
    exprFinal = exprPC[!(duplicated(exprPC$gene) | duplicated(exprPC$gene, fromLast = TRUE)),]

    #存檔，作為後續分析使用
    write.csv(exprFinal, '00_ExpectedCnt.csv')
```

### 準備臨床資料
這邊我們取腫瘤的淋巴管侵犯的特徵來分析。
```r
    names(filterTCGA02)
    #keep "Lymphatic invasion"
    varClinKeep = c('sampleID', 'lymphaticinvasion')
    clinDF01 = as.data.frame(do.call(cbind, filterTCGA02)) #因為filterTCGA02屬於data.table，可以用do.call()
    clinFinal = clinDF01[varClinKeep]
```

### 找尋缺值的數據，補NA
```r
    colSums(clinFinal == "")

    colSums(is.na(clinFinal))  

    NA -> clinFinal[clinFinal=='']
    colSums(is.na(clinFinal))
    table(clinFinal$lymphaticinvasion)  
```
### 將Yes/No 替換成1/0，以用作後需分析使用
```r
    clinFinal$lymphaticinvasion = if_else(clinFinal$lymphaticinvasion == 'YES', 1,0, missing = NULL)
    table(clinFinal$lymphaticinvasion)

```
到此終於告一段落啦，後面就可以無痛進行差異性基因分析或是WGCNA了！

# 結論
UCSCXenaTools是一個功能強大且靈活的工具，讓我們能夠在癌症基因組研究的道路上如虎添翼。在處理TCGA、GTEx 等大規模基因數據時，這個套件不僅簡化了繁瑣的數據篩選和整合流程，還提供了強大的數據搜索和下載功能，極大地提升了分析效率。

這樣的數據處理方法不僅適用於大腸癌研究，還能靈活地應用於其他癌症類型，甚至來可以下載近年十分熱門的單細胞數據。