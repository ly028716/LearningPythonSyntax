# 函数

## 定义与调用
### 定义函数
# 在Python中，可以使用`def`关键字来定义函数。
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # 输出: Hello, Alice!

### 调用函数
# 定义了函数之后，可以通过函数名加上括号来调用函数。
result = greet("Bob")
print(result)  # 输出: Hello, Bob!

## 参数传递
### 位置参数
# 位置参数是最常见的参数类型，它们按照顺序传递给函数。
def add(a, b):
    return a + b

print(add(3, 5))  # 输出: 8

### 关键字参数
# 关键字参数允许通过参数名称指定参数值，这样可以不按顺序传递参数。
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Buddy")  # 输出: I have a dog named Buddy.

### 默认参数值
# 可以在定义函数时为参数提供默认值。
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Buddy")  # 输出: I have a dog named Buddy.
describe_pet(pet_name="Whiskers", animal_type="cat")  # 输出: I have a cat named Whiskers.


## 返回值
### 返回简单值
# 函数可以返回一个值，这个值可以是任何数据类型。
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print(result)  # 输出: 24

### 返回多个值
# 函数可以通过返回一个元组来返回多个值。
def calculate(a, b):
    return a + b, a - b, a * b

sum_result, difference, product = calculate(10, 5)
print(sum_result)     # 输出: 15
print(difference)     # 输出: 5
print(product)        # 输出: 50

### 返回字典
# 函数也可以返回字典。
def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person("Jimi", "Hendrix")
print(musician)  # 输出: {'first': 'Jimi', 'last': 'Hendrix'}


# 以上内容涵盖了Python中的主要函数概念，包括定义与调用、参数传递以及返回值。