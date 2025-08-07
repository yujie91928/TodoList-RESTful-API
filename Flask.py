from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'  # 資料庫檔案
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 關閉警告

db = SQLAlchemy(app)

# 定義 Todo 模型（資料表結構）
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

#首頁顯示文字
@app.route("/")
def home():
    return "Hello, Flask!"

#GET 方法：取得完整代辦清單
@app.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    result = []
    for todo in todos:
        result.append({
            "id": todo.id,
            "title": todo.title,
            "completed": todo.completed
        })
    return jsonify(result)

#POST 方法：新增一筆代辦事項
@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    new_todo = Todo(
        title=data.get("title"),
        completed=False
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({
        "id": new_todo.id,
        "title": new_todo.title,
        "completed": new_todo.completed
    }), 201

#PUT 方法：更新一筆代辦事項
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()
    todo = Todo.query.get(todo_id)
    
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    # 更新欄位
    todo.title = data.get("title", todo.title)
    todo.completed = data.get("completed", todo.completed)

    db.session.commit()

    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    })

#DELETE 方法：刪除一筆代辦事項
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)

    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()

    return jsonify({
        "message": f"Todo {todo_id} deleted successfully."
    })

if __name__ == "__main__":
    # 初始化資料庫
    with app.app_context():
        db.create_all()

    #啟動 Flask 伺服器    
    app.run(debug=True)