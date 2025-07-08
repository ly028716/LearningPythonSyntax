# Pandas 教程

## Pandas基础
# Pandas是Python中用于数据处理和数据分析的一个强大库。它提供了两种主要的数据结构：`Series`（一维）和`DataFrame`（二维），非常适合处理表格数据。
import pandas as pd
import numpy as np  # 添加numpy导入以解决NameError

# 创建一个Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

## Series和DataFrame

### Series
# `Series`是一个类似于一维数组的对象，由一组数据和一组与之对应的索引组成。

# 创建一个带有自定义索引的Series
data = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(data)

### DataFrame
# `DataFrame`是一个表格型数据结构，可以看作是由多个`Series`组成的字典。

# 创建一个DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)

## 数据清洗
# 数据清洗是数据预处理的重要步骤，包括处理缺失值、去除重复数据等。

### 处理缺失值
# 检测缺失值
print(df.isnull())

# 删除包含缺失值的行
df_cleaned = df.dropna()

### 去除重复数据
# 检测重复行
duplicates = df.duplicated()

# 删除重复行
df_unique = df.drop_duplicates()

## 数据分析
# Pandas提供了多种数据分析方法，如统计描述、分组操作等。

### 统计描述
# 获取统计数据
print(df.describe())

### 分组操作
# 分组并计算平均值
grouped = df.groupby('Name').mean()
print(grouped)

# 以上内容涵盖了Pandas的基础知识，包括创建`Series`和`DataFrame`、数据清洗以及基本的数据分析方法。