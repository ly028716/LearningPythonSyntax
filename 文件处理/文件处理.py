# 文件处理

## 打开与读取文件

### 打开文件
# 在Python中，可以使用内置的`open()`函数来打开文件。
file = open("example.txt", "r")

### 读取文件
# 使用`read()`方法可以读取文件的全部内容。
content = file.read()
print(content)
file.close()

### 逐行读取文件
# 使用`readline()`方法可以逐行读取文件。
file = open("example.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

### 使用with语句
# 推荐使用`with`语句来自动管理文件的关闭。

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

## 写入文件
### 写入模式
# 使用写入模式(`"w"`)会覆盖现有文件或创建新文件。

with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

### 追加模式
# 使用追加模式(`"a"`)会在现有文件的末尾添加内容。
with open("example.txt", "a") as file:
    file.write("\nAppending a new line.")

### 写入多行
# 可以使用`writelines()`方法一次性写入多行。
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)

## 文件与目录操作
### 获取当前工作目录
# 使用`os.getcwd()`可以获取当前的工作目录。
import os

print(os.getcwd())

### 列出目录内容
# 使用`os.listdir()`可以列出指定目录下的所有文件和子目录。
print(os.listdir("."))

### 创建目录
# 使用`os.mkdir()`可以创建一个新的目录。
os.mkdir("new_directory")

### 删除目录
# 使用`os.rmdir()`可以删除一个空目录。
os.rmdir("new_directory")

### 检查文件是否存在
# 使用`os.path.exists()`可以检查文件或目录是否存在。
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")

### 获取文件大小
# 使用`os.path.getsize()`可以获取文件的大小（以字节为单位）。
print(os.path.getsize("example.txt"))

# 以上内容涵盖了Python中的主要文件处理操作，包括打开与读取文件、写入文件以及文件与目录操作。