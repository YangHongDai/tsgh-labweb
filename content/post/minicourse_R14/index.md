---
title: 迷你課程:R語言-14~ggplot2
date: 2025-07-02
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look


## 課前準備
```r
install.packages("ggplot2")   # 若尚未安裝
library(ggplot2)
```
## ggplot2 基本觀念（Grammar of Graphics）
- 三要素：資料（data）＋ 幾何物件（geom）＋ 映射（aes）。
- 延伸元素：統計轉換（stat）、位置調整（position）、座標系（coord）、分面（facet）、比例尺（scale）、主題（theme）。

## 基本模板：
不同的元素之間用`+`號連接。
```r
ggplot(data = <Data>) +
  <Geom_Function>(mapping = aes(<Mappings>), stat = <Stat>, position = <Position>) +
  <Coordinate_Function> +
  <Facet_Function> +
  <Scale_Function> +
  <Theme_Function>
```

## 常用輔助：
- last_plot() 取得上一張圖
- ggsave("plot.png", width=5, height=5) 儲存

## 第 2 章｜Aesthetics（美學映射）
- 常用參數包括：x, y, color, fill, size, linewidth, linetype, shape, alpha, label, group 等等。
- 顏色可用名稱或 `HEX`
- linetype 0–6
- shape 整數或名稱（0–25 等）。

## 第 3 章｜Geoms（幾何物件）與常見圖形
#### 3.1 圖形基本件
- geom_blank() / expand_limits()：統一座標範圍
- geom_curve(), geom_path(), geom_polygon(), geom_rect(), geom_ribbon()
- 參考線與線段：geom_abline(), geom_hline(), geom_vline(), geom_segment(), geom_spoke()

#### 3.2 單一變數（連續）
- 直方圖：geom_histogram(binwidth=5)
- 密度圖：geom_density()
- 頻率多邊形：geom_freqpoly()
- QQ Plot：geom_qq(aes(sample = var))

#### 3.3 單一變數（離散）
- 長條圖：geom_bar()

#### 3.4 兩變數（皆連續）
散佈圖：geom_point()
平滑線：geom_smooth(method = lm)
標籤：geom_text() / geom_label()
邊際刻度：geom_rug()
分位數回歸：geom_quantile()

#### 3.5 一離散 × 一連續
- 分組長條：geom_col()
- 盒鬚圖：geom_boxplot()
- 小提琴：geom_violin()
- 點帶圖：geom_dotplot(binaxis="y", stackdir="center")

#### 3.6 兩變數（皆離散）
- 點數加權：geom_count()
- 抖動：geom_jitter(width=, height=)

#### 3.7 雙變數分佈（連續×連續）
- 2D 直方熱圖：geom_bin2d(binwidth=c(dx, dy))
- 2D 密度等高線/填色：geom_density_2d(), stat_density_2d(geom="polygon")
- 六角格：geom_hex()

#### 3.8 時間序列/連續函數
- 面積圖：geom_area()
- 折線：geom_line()
- 階梯：geom_step(direction="hv")

#### 3.9 誤差視覺化
- geom_errorbar(), geom_pointrange(), geom_linerange(), geom_crossbar()

#### 3.10 地圖（sf）
```r
library(sf)
nc <- sf::st_read(system.file("shape/nc.shp", package = "sf"))
ggplot(nc) + geom_sf(aes(fill = AREA))
```

#### 3.11 第三變數（等高/格點）
- geom_contour(), geom_contour_filled(), geom_tile(), geom_raster()

## 第 4 章｜Stats（統計轉換）
幾乎每個 geom 都有預設 stat，也可直接用 `stat_*()`。
- `after_stat(name)`：把統計結果映射到美學。
常見例子：
```r
stat_bin(binwidth=1)           # 直方統計
stat_count(width=1)            # 離散計數
stat_density(adjust=1)         # 密度估計
stat_bin_2d(bins=30); stat_bin_hex(bins=30)
stat_density_2d(contour=TRUE, n=100)
stat_ellipse(level=0.95)
stat_summary(fun.data="mean_cl_boot")
stat_smooth(method="lm", formula = y ~ x, se=TRUE, level=0.95)
stat_function(fun = dnorm, n = 20, geom = "point")
stat_ecdf(n = 40)
```

## 第 5 章｜Scales（比例尺）
- 通用：`scale_*_continuous()`, `scale_*_discrete()`, `scale_*_binned()`, `scale_*_identity()`, `scale_*_manual(values=)`
- 日期時間：scale_*_date(), scale_*_datetime()
- X/Y 位置：scale_x_log10(), scale_x_reverse(), scale_x_sqrt()
- `顏色/填色（離散）`：`scale_fill_brewer(palette="Blues")`, `scale_fill_grey()`
- `顏色/填色（連續）`：`scale_fill_gradient()`, gradient2(), gradientn(), distiller()
- 形狀與大小：scale_shape(), scale_size(), scale_radius(), scale_size_area(max_size=)
範例（自訂圖例與順序）：
```r
p <- ggplot(mpg, aes(fl)) + geom_bar(aes(fill = fl))
p + scale_fill_manual(
  values = c("skyblue","royalblue","blue","navy"),
  limits = c("d","e","p","r"),
  breaks = c("d","e","p","r"),
  name = "fuel",
  labels = c("D","E","P","R")
)
```

## 第 6 章｜座標系（Coordinate Systems）
- coord_cartesian(xlim=, ylim=)：不刪資料 的縮放（推薦）
- coord_fixed(ratio=) 固定長寬比
- 翻轉座標：把 x、y 對調映射
- 極座標：coord_polar(theta="x")
- 轉換：coord_trans(y="sqrt")
- 地理 CRS：coord_sf()

## 第 7 章｜位置調整（Position Adjustments）
- position = "stack" | "fill" | "dodge" | "jitter" | "nudge"
函數形式可自訂寬度：
- geom_bar(position = position_dodge(width = 1))
- geom_point(position = position_jitter(width=.2, height=0))

## 第 8 章｜主題（Themes）
- 快速主題：theme_bw(), theme_gray(), theme_dark(), theme_classic(), theme_light(), theme_linedraw(), theme_minimal(), theme_void()
自訂：
- theme(panel.background = element_rect(fill = "blue"))
labs(title="Title") + theme(plot.title.position="plot")

## 第 9 章｜分面（Faceting）
```r
p <- ggplot(mpg, aes(cty, hwy)) + geom_point()
p + facet_grid(. ~ fl)
p + facet_grid(year ~ .)
p + facet_grid(year ~ fl)
p + facet_wrap(~ fl)
# 可用 scales = "free" / "free_x" / "free_y"
# 標籤客製：
p + facet_grid(. ~ fl, labeller = label_both)
p + facet_grid(fl ~ ., labeller = label_bquote(alpha ^ .(fl)))
```

## 第 10 章｜標籤與圖例（Labels & Legends）
```r
p + labs(
  x = "新X標籤", y = "新Y標籤",
  title = "主標題", subtitle = "副標題",
  caption = "圖下註解", alt = "替代文字"
)
p + annotate("text", x=8, y=9, label="A")
p + guides(x = guide_axis(n.dodge = 2))
p + guides(fill = "none")                 # 移除圖例
p + theme(legend.position = "bottom")
p + scale_fill_discrete(name="Title", labels=c("A","B","C","D","E"))
```

## 第 11 章｜縮放（Zooming）
- 推薦：coord_cartesian(xlim=c(0,100), ylim=c(10,20))（不剪資料）
- 會剪資料的做法：xlim()/ylim() 或 scale_x_continuous(limits=)。
補充：版本資訊
ggplot2 版本示例：packageVersion("ggplot2") → 3.5.2（你的貼文所示）。

## 實作練習
#### 練習 1｜從散點到發表級別
```r
p <- ggplot(mpg, aes(cty, hwy, color = class)) +
  geom_point(alpha = .7) +
  geom_smooth(method = lm, se = TRUE) +
  scale_color_brewer(palette = "Set2", name = "車型") +
  labs(x="市區油耗", y="高速油耗", title="城市 vs 高速油耗") +
  theme_classic(base_size = 12)
p
```

#### 練習 2｜比較分布
```r
ggplot(mpg, aes(class, hwy, fill = class)) +
  geom_violin(trim = FALSE, alpha = .7) +
  geom_boxplot(width = .15, outlier.shape = NA, color = "grey20") +
  guides(fill = "none") +
  theme_minimal()
```

#### 練習 3｜雙變數熱圖
```r
ggplot(diamonds, aes(carat, price)) +
  geom_bin2d(binwidth = c(.25, 500)) +
  scale_fill_distiller(palette = "Blues") +
  theme_bw()
```
## 常見排錯 Tips
1. 出現`「離散變數用到連續比例尺」`：確認 aes() 映射的變數型別（as.factor() / as.numeric()）。
2. `圖例太擠`：guide_axis(n.dodge=2) 或`旋轉角度` theme(axis.text.x = element_text(angle=45, hjust=1))。
3. 資料被裁掉：用 `coord_cartesian()` 取代 xlim()/ylim()。