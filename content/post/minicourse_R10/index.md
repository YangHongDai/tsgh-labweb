---
title: 迷你課程:R語言-10~繪圖
date: 2025-03-07
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: true
---
<!--more-->
## Quick look
R 提供了強大的繪圖功能，透過不同的函數和參數設定，我們可以 靈活控制圖形輸出。本篇教學將從最基本的 圖形設備（Graphics Device）、基礎繪圖函數、圖形參數（Graphical Parameters），到 高級繪圖技巧（如座標軸自訂、圖形裝飾），帶你全面掌握 R 的繪圖機制。

## R 的圖形設備（Graphics Device）
在 R 中，所有的圖形繪製都需要在`圖形設備（Graphics Device）`上完成。當我們執行繪圖函數（如 plot()），R 會自動開啟一個圖形設備，然後在其上繪製圖形。

#### 開啟圖形設備
不同的作業系統有不同的 預設圖形設備：
- Windows: windows()
- Mac: quartz()
- Linux: X11()
- pdf()
- postscript()
- bitmap()
- pictex()
- svg()
- png()
- jpeg()
- bmp()
- tiff()

此外，我們可以直接使用 `dev.new()` 來開啟通用的預設圖形設備，也就是會根據你的作業系統，自動選擇適當的圖形設備 
```r
dev.new(width = 7, height = 7, xpos = 1000, ypos = 200)  # 指定視窗大小與位置
```
#### 列出目前的圖形設備
```r
dev.list()  # 顯示所有已開啟的圖形設備
```
#### 關閉圖形設備
```r
dev.off()  # 關閉當前的圖形設備 如果接連開了三個，每執行一次關一個
```
#### 關閉所有圖形設備
類似 RStudio 右上角的`「清除圖形」。`
```r
graphics.off()  
```
## 預設
可以用.options()來預設圖形設備參數
```r
quartz.options(xpos=1000, ypos=500)
quartz()
quartz.options(reset = TRUE)
```

---
## 儲存繪圖
R 允許我們將圖形儲存為不同的格式，例如：
```r
pdf("plot1.pdf", width = 7, height = 7)  # 儲存為 PDF 這種稱為隱形graphic device
plot(rnorm(10), rnorm(10))
dev.off()  # 關閉設備並存檔
```
plot() 或hist()在執行時，會找尋當前有沒有graphic device，如果有就畫在上面，如果沒有，就新增一個，畫在上面。
```r
jpeg("plot1.jpeg", width = 700, height = 700)  # 儲存為 JPEG
plot(rnorm(10), rnorm(10))
dev.off()
```
---

## plot() 函數的基本用法
plot() 是 R 最基礎的繪圖函數，可用來繪製`散佈圖（scatter plot）`。
```r
plot(rnorm(10), rnorm(10))  # 繪製 10 個隨機點
```

## 我們可以透過 type 參數設定不同類型的圖：
```r
plot(x1, x2, type = "l")  # 折線圖（line）
plot(x1, x2, type = "b")  # 點+線（both）
plot(x1, x2, type = "o")  # 點在線上（overlap）
plot(x1, x2, type = "n")  # 不畫點，只設置坐標軸（no plotting）
```
例如，今天有一個函式:
```r
circle_points <-function(n=12, noise=0.2){
      theta <- 2*pi*seq(0,1,length.out=n+1)[-1]
      x1 <- cos(theta) + noise*rnorm(n)
      x2 <- sin(theta) + noise*rnorm(n)
      return(list(x1=x1, x2=x2))
}
circ <- circle_points()
x1 <-circ$x1
x2 <-circ$x2

plot(x1,x2) #default type='p' 表示points
plot(x1,x2, type='l')
plot(x1,x2, type='b')
```
![Fig1](Fig1.png '圖一')
![Fig2](Fig2.png '圖二')
![Fig3](Fig3.png '圖三')


## 調整 X 軸與 Y 軸範圍: xlim and ylim
```r
plot(x1, x2, xlim = c(-2,2), ylim = c(-2,2))
```
## 更改軸標題: xlab and ylab
```r
plot(x1, x2, xlab = "水平位置 (cm)", ylab = "垂直位置 (cm)")
```

## points() 和 lines() 函數
當我們已經繪製了圖形時，可以用 `points()` 或 `lines()` 來`增加更多的點或線`。
```r
plot(x1, x2, xlim = c(-1.5,1.5), ylim = c(-1.5,1.5))
points(circ$x1, circ$x2, pch = 2)  # 添加三角形點
lines(c(x1, x1[1]), c(x2, x2[1]), col = "magenta")  # 畫出封閉的圓形線
```
![Fig4](Fig4.png '圖四')

## text() 與 mtext() 標註
在圖中添加文字
```r
plot(x1, x2, xlim = c(-1.5,1.5), ylim = c(-1.5,1.5))
text(x1, x2 - 0.3, LETTERS[1:12])  # 加入標記 A~L
```
![Fig5](Fig5.png '圖五')

## 在圖的邊界加上標題
```r
plot(x1, x2, xlim = c(-1.5,1.5), ylim = c(-1.5,1.5))
mtext("Important", side = 3, line = 0) # 下左上右->1,2,3,4
mtext("Important", side = 3, line = 1.5, font = 2, cex = 1.5)
```
![Fig6](Fig6.png '圖六')

其他參數還包括，polygon、rect、segments、abline、arrows，有興趣可以再去看。

## 自訂座標軸（axis）
```r
plot(x1, x2, axes = FALSE)  # 隱藏座標軸
#隱藏後用axis()重新定義
axis(1, at = -1:1, labels = c("左", "中", "右"))  # 自訂 X 軸標籤
axis(2, at = seq(-1,1,by=0.1))  # Y 軸細刻度
box()  # 添加邊框
```
有時候，定義了axis後再加入邊框會有部份重疊的狀況，此時可以調整axis的線粗度為0，保持標記即可：
```r
axis(1,lwd=0,lwd.ticks=1)
axis(2,lwd=0,lwd.ticks=1)
```

## par() 設定全局繪圖參數
```r
par(col = "gray", col.axis = "magenta", pch = 4, mar = c(6,6,1,1))
par(mfrow=c(2,2)) #會繪製2 x 2的圖
plot(x1, x2)  # 使用灰色點和洋紅色座標軸
```
如果以dev.off()將plots關閉，再重繪，系統會忘記par()的設定，因此只適用於當前的graphic device。


---
## 練習：使用 Hershey 字體繪製時鐘
以下範例繪製了一個時鐘，並使用 Hershey 字體為時鐘標記數字。

#### 設定畫布
```r
par(mar = c(0,0,0,0))
plotsize <- 1.5
plot(0, type = "n", xlim = plotsize * c(-1,1), ylim = plotsize * c(-1,1), axes = FALSE, ann = FALSE)
```

### 添加 1~12 的數字
circ <- circle_points(n = 12, noise = 0)
x1 <- circ$x1
x2 <- circ$x2
nums <- c(2,1, 12:3)
text(x1, x2, nums, cex = 3.0, vfont = c("serif", "bold"))

### 繪製指針
points(0,0, pch = 16, cex = 4)
arrows(0, 0, 0.7*cos(2*pi*5/12), 0.7*sin(2*pi*5/12), lwd = 8)  # 時針
arrows(0, 0, 0.85*cos(2*pi*1/12), 0.85*sin(2*pi*1/12), lwd = 4)  # 分針

### 添加公司名稱
text(0, 0.5, "WatchCo", vfont = c("serif", "plain"), cex = 1.75)

### 添加邊框
rect(-1.25, -1.25, 1.25, 1.25, border = 2, lwd = 12)

---
## 課程小結
plot() 是 R 最基本的繪圖函數，但可以透過 points()、lines()、text() 來進一步擴展功能。
par() 可用來設定全局繪圖參數，影響多個圖形的顯示方式。
座標軸可以自訂，並且可以使用 Hershey 字體進行高級標註。
R 允許我們輸出到 PDF 或影像格式，方便匯出分析結果。