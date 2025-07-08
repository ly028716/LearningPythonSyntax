# 控制结构

## 条件语句
# Python中的条件语句使用`if`、`elif`和`else`关键字来实现。

### if语句
x = 10
if x > 0:
    print("x is positive")

### if-else语句
x = -5
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

### if-elif-else语句
x = 0
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

## 循环语句
# Python提供了两种主要的循环语句：`for`循环和`while`循环。

### for循环
# `for`循环用于遍历任何序列的项目，如列表或字符串。

#### 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#### 遍历字符串
for char in "hello":
    print(char)

#### range()函数
for i in range(5):
    print(i)  # 输出0到4

### while循环
# `while`循环在给定的布尔条件为真时重复执行代码块。

#### 基本while循环
i = 0
while i < 5:
    print(i)
    i += 1

#### break语句
# `break`语句用于提前退出循环。
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

#### continue语句
# `continue`语句用于跳过当前循环迭代。
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 只打印奇数

## 控制流工具
### else子句
# `for`和`while`循环可以有一个可选的`else`子句，它仅在循环条件变为假时执行。

#### for-else
for i in range(5):
    print(i)
else:
    print("Loop finished")

#### while-else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

### pass语句
# `pass`语句是一个空操作；当它被执行时，没有任何事情发生。
def my_function():
    pass  # 暂时不实现函数功能

# 以上内容涵盖了Python中的主要控制结构，包括条件语句、循环语句以及控制流工具。