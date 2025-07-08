# Flask 教程

## Flask基础
# Flask是一个轻量级的Web应用框架，使用Python编写。它简单易用，适合快速开发小型到中型的Web应用。

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)


## 路由和模板
### 定义路由
# Flask使用装饰器来定义路由。
@app.route('/hello')
def show_hello():
    return 'Hello, Flask!'

### 使用模板
# Flask使用Jinja2模板引擎来渲染HTML页面。
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

#### `greet.html` 模板示例
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Greeting</title>
# </head>
# <body>
#     <h1>Hello, {{ name }}!</h1>
# </body>
# </html>


## 表单处理
# Flask可以轻松处理表单数据。

### 接收表单数据
from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'Login for {username} with password {password}'

## 数据库集成
# Flask可以与多种数据库集成，以下是使用SQLite的示例。

### 连接数据库
import sqlite3
def get_db():
    db = sqlite3.connect('flask_app.db')
    db.row_factory = sqlite3.Row
    return db

### 查询数据库
@app.route('/users')
def list_users():
    db = get_db()
    cur = db.execute('SELECT * FROM users')
    users = cur.fetchall()
    return render_template('list_users.html', users=users)

# 以上内容涵盖了Flask的基础知识，包括创建应用、定义路由、使用模板、处理表单数据以及数据库集成的方法。