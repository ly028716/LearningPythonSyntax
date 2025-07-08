# FastAPI 教程

## FastAPI基础
# FastAPI是一个现代的、快速（高性能）的Web框架，基于Python类型提示构建，并使用异步请求处理。
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

## 路由和请求处理

### 定义路由
# FastAPI使用装饰器来定义路由。
@app.get("/users")
async def read_users():
    return ["Alice", "Bob", "Charlie"]

### 请求方法
# FastAPI支持多种HTTP请求方法，如`GET`、`POST`、`PUT`和`DELETE`。
@app.post("/items")
async def create_item(item: dict):
    return {"message": "Item created", "item": item}

## 请求验证
# FastAPI利用Pydantic模型进行自动请求验证。
### 使用Pydantic模型
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items")
async def create_item(item: Item):
    return {"message": "Item created", "item": item}

## 自动化测试
# FastAPI应用可以轻松地进行自动化测试。

### 使用pytest进行测试
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# 以上内容涵盖了FastAPI的基础知识，包括创建应用、定义路由、处理请求以及自动化测试的方法。