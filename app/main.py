from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2 import pool

app = Flask(__name__)

# Database connection pool
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,
    user="postgres",
    password="password",
    host="db",
    port="5432",
    database="tasks_db"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, description FROM tasks")
            tasks = cur.fetchall()
            return jsonify([{'id': t[0], 'title': t[1], 'description': t[2]} for t in tasks])
    finally:
        db_pool.putconn(conn)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id",
                (title, description)
            )
            task_id = cur.fetchone()[0]
            conn.commit()
            return jsonify({'id': task_id, 'title': title, 'description': description}), 201
    finally:
        db_pool.putconn(conn)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE tasks SET title = %s, description = %s WHERE id = %s",
                (title, description, id)
            )
            conn.commit()
            return jsonify({'id': id, 'title': title, 'description': description})
    finally:
        db_pool.putconn(conn)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM tasks WHERE id = %s", (id,))
            conn.commit()
            return jsonify({'message': 'Task deleted'})
    finally:
        db_pool.putconn(conn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
