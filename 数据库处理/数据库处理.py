# 数据库处理

## MySQL教程

### 连接MySQL数据库
# 在Python中，可以使用`mysql-connector-python`库来连接MySQL数据库。
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)

# 创建游标对象
mycursor = mydb.cursor()

# 使用`CREATE DATABASE`语句来创建一个新的数据库。
curser = mydb.cursor()

# 检查数据库是否存在
mycursor.execute("SHOW DATABASES")
existing_dbs = [db[0] for db in mycursor.fetchall()]

if 'mydatabase' not in existing_dbs:
    mycursor.execute("CREATE DATABASE mydatabase")

# 选择要使用的数据库
mydb.database = 'mydatabase'

### 创建数据表
# 使用`CREATE TABLE`语句来创建一个新的数据表。
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

### 插入数据
# 使用`INSERT INTO`语句向数据表中插入数据。
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

### 查询数据
# 使用`SELECT`语句从数据表中查询数据。
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

### 更新数据
# 使用`UPDATE`语句更新数据表中的数据。
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

### 删除数据
# 使用`DELETE FROM`语句删除数据表中的数据。
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

## MongoDB教程

from pymongo import MongoClient

### 连接MongoDB数据库
# 在Python中，可以使用`pymongo`库来连接MongoDB数据库。
client = MongoClient('mongodb://localhost:27017/')
print(client)

### 创建数据库
# 在MongoDB中，数据库在首次存储数据时自动创建。
db = client['mydatabase']
print(db)

### 创建集合
# 在MongoDB中，集合在首次存储数据时自动创建。
collection = db['customers']
print(collection)

### 插入文档
# 使用`insert_one()`或`insert_many()`方法向集合中插入文档。
doc = {"name": "John", "address": "Highway 21"}
x = collection.insert_one(doc)

print(x.inserted_id)

### 查询文档
# 使用`find_one()`或`find()`方法从集合中查询文档。
x = collection.find_one()
print(x)

for x in collection.find():
  print(x)

### 更新文档
# 使用`update_one()`或`update_many()`方法更新集合中的文档。
query = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

collection.update_one(query, newvalues)

for x in collection.find():
  print(x)

### 删除文档
# 使用`delete_one()`或`delete_many()`方法删除集合中的文档。
query = { "address": "Mountain 21" }

collection.delete_many(query)

for x in collection.find():
  print(x)

# 以上内容涵盖了Python中处理MySQL和MongoDB数据库的基本操作，包括连接数据库、创建数据库和数据表（或集合）、插入数据、查询数据、更新数据以及删除数据。