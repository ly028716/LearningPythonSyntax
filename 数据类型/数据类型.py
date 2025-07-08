# 数据类型

## 数值类型
# Python支持多种数值类型，包括整数、浮点数和复数。

### 整数
a = 10
b = -5

### 浮点数
c = 3.14
d = -0.001

### 复数
e = 3 + 4j
f = -2j

## 字符串
# 字符串是由字符组成的序列，可以用单引号或双引号定义。

### 单引号
s1 = 'Hello'

### 双引号
s2 = "World"

### 多行字符串
s3 = """This is
a multi-line
string."""

## 列表与元组
# 列表和元组是用于存储多个项目的有序集合。

### 列表
# 列表是可变的，可以使用方括号定义。

list1 = [1, 2, 3]
list2 = ['apple', 'banana', 'cherry']

### 元组
# 元组是不可变的，可以使用圆括号定义。
tuple1 = (1, 2, 3)
tuple2 = ('apple', 'banana', 'cherry')

## 字典
# 字典是无序的键值对集合，使用花括号定义。

### 定义字典
dict1 = {"name": "Alice", "age": 25}
dict2 = {"brand": "Ford", "model": "Mustang", "year": 1964}

### 访问字典值
print(dict1["name"])  # 输出: Alice
print(dict2["model"])  # 输出: Mustang

### 修改字典值
dict1["age"] = 26

### 添加新的键值对
dict1["city"] = "New York"

### 删除键值对
del dict1["age"]

## 集合
# 集合是无序的不重复元素集，使用花括号定义。

### 定义集合
set1 = {1, 2, 3}
set2 = {'apple', 'banana', 'cherry'}

### 添加元素
set1.add(4)

### 删除元素
set1.remove(2)

### 集合操作

#### 并集
set3 = set1.union(set2)

#### 交集
set4 = set1.intersection(set2)

# 以上内容涵盖了Python中的主要数据类型，包括数值类型、字符串、列表、元组、字典和集合。