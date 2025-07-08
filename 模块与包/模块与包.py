# 模块与包

## 模块导入

### 导入模块
# 在Python中，可以使用`import`关键字来导入模块。
import math

print(math.sqrt(16))  # 输出: 4.0

### 导入特定函数
# 可以使用`from ... import ...`语法从模块中导入特定的函数或变量。

from math import sqrt

print(sqrt(16))  # 输出: 4.0

### 导入所有内容
# 使用`from ... import *`可以从模块中导入所有内容。
from math import *

print(sqrt(16))  # 输出: 4.0

### 使用别名
# 可以为导入的模块或函数指定一个别名。

import math as m

print(m.sqrt(16))  # 输出: 4.0

from math import sqrt as square_root

print(square_root(16))  # 输出: 4.0

## 标准库模块
# Python标准库包含了许多有用的模块，以下是一些常见的例子。

### `os`模块
# `os`模块提供了许多与操作系统交互的功能。
import os

print(os.getcwd())  # 获取当前工作目录

### `sys`模块
# `sys`模块提供了访问解释器相关的变量和函数。

import sys

print(sys.version)  # 获取Python版本信息

### `datetime`模块
# `datetime`模块用于处理日期和时间。
import datetime

now = datetime.datetime.now()
print(now)  # 输出当前日期和时间

### `random`模块
# `random`模块提供了生成随机数的功能。
import random
print(random.randint(1, 10))  # 输出1到10之间的随机整数

## 创建自己的包
### 创建包结构
# 包是一种组织模块的方法，通常包含一个名为`__init__.py`的文件。假设我们要创建一个名为`my_package`的包，其结构如下：
# my_package/
# │
# ├── __init__.py
# ├── module1.py
# └── module2.py

### 包中的模块

#### `module1.py`

# my_package/module1.py
def say_hello():
    print("Hello from module1!")

#### `module2.py`
# my_package/module2.py
def say_goodbye():
    print("Goodbye from module2!")

### 使用自定义包
# 创建完包后，可以在其他Python脚本中使用它。
# main.py
from my_package import module1, module2

module1.say_hello()  # 输出: Hello from module1!
module2.say_goodbye()  # 输出: Goodbye from module2!

# 以上内容涵盖了Python中的主要模块与包的概念，包括模块导入、标准库模块以及创建自己的包。