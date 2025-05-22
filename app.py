from flask import Flask, render_template, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_FILE = 'data_block/transactions.db'

# 初始化数据库逻辑
def init_db():
    if not os.path.exists(DB_FILE):
        print("📌 数据库不存在，开始初始化")
        # 确保目录存在
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        conn = sqlite3.connect(DB_FILE)
        with open('schema.sql', 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.close()
    else:
        print("ℹ️ 数据库已存在，跳过初始化")

# 应用启动时初始化数据库
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transactions')
def get_transactions():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cur.fetchall()
    return jsonify([dict(row) for row in rows])

if __name__ == '__main__':
    app.run(debug=True)