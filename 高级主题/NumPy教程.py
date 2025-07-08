# NumPy 教程

## NumPy基础
# NumPy是Python中用于科学计算的一个基本包。它提供了一个多维数组对象（ndarray），以及多种派生对象（如掩码数组和矩阵），还包括各种各样的例程，用于快速操作这些数组。

import numpy as np

# 创建一个一维数组
a = np.array([1, 2, 3])
print(a)

# 创建一个二维数组
b = np.array([[1, 2], [3, 4]])
print(b)


## 数组操作
### 数组属性

# - `ndim`：数组的维度数量。
# - `shape`：数组的尺寸，返回一个元组。
# - `size`：数组中的元素总数。
# - `dtype`：数组中元素的数据类型。
# - `itemsize`：每个元素的大小（以字节为单位）。
print("Array a ndim:", a.ndim)
print("Array a shape:", a.shape)
print("Array a size:", a.size)
print("Array a dtype:", a.dtype)
print("Array a itemsize:", a.itemsize)

### 数组索引
# 与Python列表类似，可以通过索引来访问和修改数组中的元素。
# 访问数组中的元素
print(a[0])  # 输出: 1

# 修改数组中的元素
a[0] = 5
print(a)  # 输出: [5 2 3]


## 数学函数
# NumPy提供了大量的数学函数，可以直接应用于数组。

### 常用数学函数
# - `np.sin()`：计算数组中每个元素的正弦值。
# - `np.cos()`：计算数组中每个元素的余弦值。
# - `np.tan()`：计算数组中每个元素的正切值。
# - `np.exp()`：计算数组中每个元素的指数值。
# - `np.sqrt()`：计算数组中每个元素的平方根。
# 计算正弦值
print(np.sin(a))

# 计算平方根
print(np.sqrt(a))

## 广播机制
# 广播机制允许不同形状的数组进行算术运算。通常情况下，较小的数组会沿着较大的数组扩展，直到它们具有相同的形状。
# 广播示例
a = np.array([1, 2, 3])
b = 2
print(a * b)  # 输出: [2 4 6]

# 以上内容涵盖了NumPy的基础知识，包括创建数组、数组属性、索引以及常用数学函数的应用。