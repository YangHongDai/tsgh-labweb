---
title: 迷你課程:PyTorch-1
date: 2025-09-12
authors: ["戴揚紘", ""]
commentable: true
categories: [PyTorch迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
參考了這個教學「[網站](https://www.learnpytorch.io/00_pytorch_fundamentals/#introduction-to-tensors)，以及我自己在Udemy購買的線上課程


## 什麼是 PyTorch？能做什麼？為何用它？
PyTorch 是一個開源的機器學習／深度學習框架，讓你用 Python 操作資料、撰寫與訓練模型。
被大量公司與研究機構採用（Meta、Tesla、Microsoft、OpenAI…），從自駕電腦視覺到農業電腦視覺皆可見。
優點：
1. 易上手、研究友善（動態計算圖、Pythonic）。
2. GPU 加速與自動微分幾乎都幫你處理好。
3. 研究社群活躍、資源多（Papers with Code 使用率高）。

資源:
1. 官方文件、論壇（discuss.pytorch.org）。
2. 課程 GitHub／Discussions（如果跟課出現版本差異或錯誤）。

---
## 安裝與版本
```python
import torch
print(torch.__version__)
```
PyTorch 版本常影響 API 細節；只要 1.10+ 大多內容都相容。若你用 Colab，通常已內建。

---
## 張量（Tensor）是什麼？
- `張量` = 數字的容器。深度學習就是不斷對張量做運算。
- `標量 (scalar)`：`0` 維（例：7）
- `向量 (vector)`：`1` 維（例：[7,7]）
- `矩陣 (matrix)`：`2` 維（例：[[7,8],[9,10]]）
- `高維張量 (tensor)`：`任意維`（例：[1,3,224,224] 影像）

#### 建立基本張量
```python
import torch

# 標量
scalar = torch.tensor(7)
print(scalar, scalar.ndim)        # tensor(7), 0
print(scalar.item())              # 取出 Python 整數 7（只適用 1 個元素）

# 向量
vector = torch.tensor([7, 7]) #方向加上大小
print(vector.ndim, vector.shape)  # 1, torch.Size([2])

# 矩陣
MATRIX = torch.tensor([[7, 8],
                       [9,10]])
print(MATRIX.ndim, MATRIX.shape)  # 2, torch.Size([2,2])

# 三維張量
TENSOR = torch.tensor([[[1,2,3],[3,6,9],[2,4,5]]])
print(TENSOR.ndim, TENSOR.shape)  # 3, torch.Size([1,3,3])
```
小技巧：看外層方括號數量可快速判斷維度數。所以三維張量那邊有三個`[[[`，所以為三維。

> 在 PyTorch：

> 每次 tensor[i] = 沿著 第 0 維選取 index = i 的切片。
> 如果張量是多維的，選出來的結果會少一個維度

```python
print(MATRIX.shape)   # (2, 2)
print(MATRIX[0].shape) # (2,)   <- 取一列，少一維

print(TENSOR.shape)    # (1, 3, 3)
print(TENSOR[0].shape) # (3, 3) <- 取一層，少一維
```


---
## 建立常見張量：隨機、全 0、全 1、range
```python
# 隨機
torch.rand(3, 4)                 # 3x4，dtype= float32

# 指定影像形狀
random_image_size_tensor = torch.rand(size = (224, 224, 3))
# 與上面同義
random_image_size_tensor = torch.rand(224, 224, 3)

# 全 0 / 全 1
torch.zeros(3, 4)
torch.ones(3, 4) ## dtype = float32

# 連續整數（左閉右開）
torch.arange(start=0, end=10, step=1)  # 0..9

# 形狀對齊衍生
x = torch.arange(10)
torch.zeros_like(x)               # 與 x 同形狀的全 0
torch.ones_like(x)                # 與 x 同形狀的全 1

```

---
## 張量 3 大屬性：shape / dtype / device
```python
t = torch.rand(3, 4, dtype=torch.float32,device=None, requires_grad=False)##requires_grad 表示是否需要追蹤梯度
print(t.shape)   # torch.Size([3,4])
print(t.dtype)   # torch.float32 (預設)
print(t.device)  # cpu 或 cuda

```
遇到錯誤先自問：形狀對嗎？資料型別對嗎？放在哪個裝置？（shape / dtype / device）

---
## 資料型別（dtype）
常見：float32（預設）、float16、float64；整數 int8/16/32/64。
精度越低 ⇒ 計算越快、模型越小，但可能較不準。
```python
float_32 = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float32)
float_16 = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16)
print(float_16.dtype)             # torch.float16

# 轉型
x = torch.arange(10., 100., 10.)
#使用tensor.type()
x_half = x.type(torch.float16) #也可以使用torch.half 與torch.float16同樣意思
x_int8 = x.type(torch.int8)
```
有時候不同的data type運算不一定會出現錯誤，例如`相加與相乘`，但仍需要小心data type的一致性。

---
## 張量運算（加減乘除、矩陣乘法）
#### 基本運算
```python
tensor = torch.tensor([1,2,3])

tensor + 10
tensor * 10

# 不會改變原 tensor，除非你重新賦值
tensor = tensor - 10

# 函數式寫法
torch.multiply(tensor, 10) 
torch.mul(tensor,10)
```
上面的element-wise 乘法建議使用`*`，比較不容易出錯。

#### 元素乘 vs 矩陣乘
```python
a = torch.tensor([1,2,3])
a * a                 # 元素乘 -> tensor([1,4,9])
torch.matmul(a, a)    # 矩陣乘 -> 1*1 + 2*2 + 3*3 = 14
torch.mm(a,a) #跟matmul同義
a @ a                 # 等同 matmul
```
使用matmul的矩陣相乘方式會比使用for loop 來運算要快很多。

#### 形狀錯誤是常態（內部維度需相等）
```python
A = torch.tensor([[1,2],[3,4],[5,6.]], dtype=torch.float32)  # 3x2
B = torch.tensor([[7,10],[8,11],[9,12.]], dtype=torch.float32) # 3x2
# torch.matmul(A, B)  # 會錯：3x2 @ 3x2 內維不合

# 轉置讓內維對上
B_T = B.T  # 2x3
out = torch.matmul(A, B_T)  # 3x2 @ 2x3 -> 3x3
```
torch.mm 是 2D 專用矩陣乘（只接受 2D），torch.matmul 支援更一般情況。

所以，矩陣相乘時：
1. 內部維度要一致。
2. 相乘後的矩陣維度為外層維度。


---
## 線性層其實就是矩陣乘
```python
torch.manual_seed(42)
linear = torch.nn.Linear(in_features=2, out_features=6)
x = A                         # A 形狀 [3,2]
y = linear(x)    
```
若把 in_features 改成 3，輸入也要對應改成 [..., 3]（或經轉置／重塑）。

---
## 聚合（min/max/mean/sum）與位置（argmin/argmax）
```python
x = torch.arange(0, 100, 10)

x.min(); x.max()
x.type(torch.float32).mean() # torch.mean()內部的datatype 不能用在torch.long dtype
x.sum()

# 位置：找出對大值與最小值的位置
t = torch.arange(10, 100, 10)
t.argmax(), t.argmin()   # 8, 0
```

---
## 形狀變換：reshape / view / stack / squeeze / unsqueeze / permute
```python
x = torch.arange(1., 8.)           # [7]
#> tensor([1., 2., 3., 4., 5., 6., 7.]) 


# reshape：回傳新的張量（可不連續記憶體時也能用）
# 這樣其實為多一層維度 tensor([[1., 2., 3., 4., 5., 6., 7.]]) 有沒有注意到外面多一層[]
x_r = x.reshape(1, 7)               # [1,7]

# view：回傳「同一塊資料的不同檢視」，**共享底層記憶體**
z = x.view(1, 7)
z[:, 0] = 5                         # 會一併改到 x

# 將多個張量疊成新維度
x_stacked = torch.stack([x, x, x, x], dim=0)  # [4,7]

# squeeze：移除所有長度為 1 的維度
x_sq = x_r.squeeze()                         # [7]

# unsqueeze：在指定位置加入長度為 1 的維度
x_us = x_sq.unsqueeze(dim=0)                 # [1,7]

# permute：重排軸順序（回傳 view，會共享資料）
img = torch.rand(224, 224, 3)                # HWC height width channel

#Shift axis 0->1,1->2, 2->0
chw = img.permute(2, 0, 1)                   # CHW
```
`view` 與 `permute` 產生的張量共享底層資料，改其中之一會同時改到另一個。

---
## 索引（Indexing）
`與 NumPy 類似`，外到內逐層 [] 或用逗號分隔維度：
```python
x = torch.arange(1,10).reshape(1,3,3)

x[0]
x[0][0] # = x[0,0]
x[0,0,:]
x[:, :, 1]   # 所有樣本的第 2 欄
x[:, 1, 1]   # 中間位置
```
這邊如果用`:`全選，會發現多一個`[]` (eg `tensor([5])`)，如果用`0`來index就不會有 (`tensor(5)`)，需要注意。

---
## 與 NumPy 互轉（共享記憶體）
```python
import numpy as np

# numpy -> torch（**共享記憶體**）
arr = np.arange(1.0, 8.0)
ten = torch.from_numpy(arr)        # 注意轉換後dtype 會跟 numpy 一致（float64->numpy default dtype）
arr = arr + 1                      # 只改 arr，不會動 ten（因重新指派 arr）

# torch -> numpy（**共享記憶體**）
t = torch.ones(7)                  # float32 (pyTorch default)
a = t.numpy()                      # 也是 float32
t = t + 1                          # 重新指派，不會改 a
```
若是裝置在 GPU 的張量，必須先 .cpu() 再 .numpy()。
如果 Tensor 在 `GPU（CUDA）` 上，必須先把資料拷回 CPU（`tensor.cpu()`），再 `.numpy()`。這一步會產生`新拷貝`，所以 不會共享記憶體；之後改 GPU 上的 tensor，NumPy 陣列不會跟著變，反之亦然。

```python
# 情況 A：CPU 張量 → 共享記憶體（零拷貝）
t = torch.ones(3)        # 在 CPU
a = t.numpy()            # a 與 t 共享同一塊 CPU 記憶體
t += 1                   # 原地修改
# a 會跟著變

# 情況 B：GPU 張量 → 必須先搬到 CPU（會拷貝，不共享）
t = torch.ones(3, device='cuda')  # 在 GPU
a = t.cpu().numpy()               # 先從 GPU 拷回 CPU，再轉 numpy（新拷貝）
t += 1                            # 改 GPU 上的 t
# a 不會變（因為 a 是拷貝，不共享）
```
結論就是，想要 NumPy 與 Tensor 共享記憶體：Tensor 必須在 CPU，而且用 非複製的轉換（tensor.numpy()）。

---
## 可重現性（Random Seed）
先設定一個random seed，然後再更新random seed看訓練結果有沒有改善，並考慮持續更換。
```python
import torch

# 平常：兩個 rand 不同
A = torch.rand(3,4)
B = torch.rand(3,4)

# 設定種子：讓隨機序列可重現
torch.manual_seed(42)
C = torch.rand(3,4)

torch.manual_seed(42)  # 若再次設同 seed
D = torch.rand(3,4)    # -> 與 C 完全相同

(C == D).all()         # True
```
觀念：設一次 seed 會固定「隨機序列」，若你要兩次抽樣結果一模一樣，就在第二次抽前再設一次同樣的 seed。在notebook的狀態，如果只在一開始設定一次，這樣會無法得到兩個相同的random number。
真正嚴格可重現性還包含 cuDNN 設定、資料載入器隨機性等（見 PyTorch reproducibility guide）。

---
## 把張量（與模型）放到 GPU / MPS（Apple Silicon）
#### 檢查裝置與裝置無關寫法
1. 核心概念
- PyTorch 本身是一個深度學習框架，計算主要透過 張量運算 (tensor operations)。
- 在 CPU 上，這些運算會調用 BLAS、MKL 等數值庫。
- 在 GPU 上，PyTorch 會調用 NVIDIA 的 CUDA 生態系。
2. 底層技術
- CUDA (Compute Unified Device Architecture)：NVIDIA 開發的 GPU 平行計算平台，讓程式能直接用 GPU 做矩陣運算。
- cuDNN (CUDA Deep Neural Network library)：針對深度學習常用操作（卷積、池化、RNN 等）做高度優化的函式庫。
- PyTorch GPU 版 就是透過 torch.cuda 把 tensor 運算轉換成 CUDA kernel，在 GPU 上執行。

> 什麼時候需要用到 Cloud Computing（AWS, 阿里雲, GCP 等）？

> 本地 GPU 不夠用，或你根本沒有 GPU 時，就需要雲端算力。常見情境：
模型太大 / 資料太多

> 本地電腦 GPU 記憶體不足（例如 8GB 無法跑大模型 BERT、ResNet-152、單細胞多組學數據）。

> 雲端可以選擇 16GB、40GB、80GB GPU（如 V100, A100, H100）。

> 多 GPU / 分布式訓練

> 本地通常只有 1 張 GPU，無法做大規模並行。
> 在雲端可以租一個多 GPU 節點（4–8 張卡），或整個集群，顯著加快訓練速度。

> 彈性使用 / 成本考量

> 如果只是偶爾需要 GPU，買一張昂貴的顯卡（比如 A100）不划算。

> 雲端隨用隨付：需要時租 1–2 天，不需要就釋放，節省硬體投資。

> 合作與可重現性

> 多人合作時，用雲端（AWS S3、阿里雲 OSS）存取資料與模型更方便。
也能部署 Notebook/環境給同事直接使用，避免本地環境差異。

```python
import torch

if torch.cuda.is_available():
    device = "cuda"              # NVIDIA GPU
elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
    device = "mps"               # Apple Silicon
else:
    device = "cpu"

print(device)
```
---
#### 張量搬移
```python
x = torch.tensor([1,2,3])        # 預設在 CPU
x_dev = x.to(device)             # 複製到指定裝置（回傳新張量）
print(x, x.device)
print(x_dev, x_dev.device)

# 若要轉成 numpy，必須在 CPU
x_cpu_np = x_dev.cpu().numpy()
```
規則：所有運算的張量要在同一裝置；要轉 NumPy 必須先 .cpu()。

#### 多 GPU
```python
torch.cuda.device_count()        # 有幾張 GPU
# 'cuda:0', 'cuda:1' ... 0-based
```
---
## 課程小結
1. 三問：出錯先問 shape? dtype? device?
2. view/permute 共享資料，修改其一會影響原張量；需要獨立請用 clone() 或 reshape()（非連續時 view 會失敗）。
3. 矩陣乘法：內維必須相等；matmul 比 mm 通用（可處理 >2D 與廣播）。
4. dtype 不合：float32 vs float16/64 常見；必要時轉型。
5. GPU→NumPy：先 .cpu() 再 .numpy()。
6. seed：要重現同一序列就重設同 seed；要不同結果就不要重設。