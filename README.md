# Flask Todo API

一個使用 Python Flask 與 SQLite 實作的簡易代辦事項（Todo List）RESTful API。

## 功能

- 取得所有代辦事項 (GET /todos)
- 新增代辦事項 (POST /todos)
- 更新代辦事項 (PUT /todos/<id>)
- 刪除代辦事項 (DELETE /todos/<id>)

## 技術堆疊

- Python 3
- Flask
- Flask-SQLAlchemy (SQLite)

## 快速開始

1. 建立虛擬環境並安裝依賴

```bash
python -m venv Flask_api
source Flask_api/bin/activate   # macOS/Linux
Flask_api\Scripts\activate      # Windows
pip install -r requirements.txt
```

2. 執行程式
```bash
python Flask.py
```
3. 使用 API
```bash
預設http://127.0.0.1:5000
```
4. API 範例
- 取得代辦事項
```bash
GET /todos
```
- 新增代辦事項
```bash
POST /todos
```
```bash
Content-Type: application/json
{
  "title": "代辦事項名稱"
}
```
- 更新代辦事項(可修改title及completed狀態)
```bash
PUT /todos/<代辦事項id>
Content-Type: application/json
{
  "title": "可修改代辦事項名稱",
  "completed": true
}
```
- 刪除代辦事項
```bash
DELETE /todos/<代辦事項id>
```