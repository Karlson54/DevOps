"""Main Flask application with PostgreSQL integration."""
import os
from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'database': os.getenv('POSTGRES_DB', 'devops_db'),
    'user': os.getenv('POSTGRES_USER', 'devops_user'),
    'password': os.getenv('POSTGRES_PASSWORD', 'devops_pass'),
    'port': os.getenv('POSTGRES_PORT', '5432')
}


def get_db_connection():
    """Create database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None


@app.route('/')
def home():
    """Home page route."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Lab 7</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            .endpoints {
                margin-top: 20px;
            }
            .endpoint {
                background-color: #ecf0f1;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }
            code {
                background-color: #34495e;
                color: #ecf0f1;
                padding: 2px 6px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello, DevOps!</h1>
            <p>Welcome to Lab 7 - Docker + PostgreSQL Web Application</p>
            
            <div class="endpoints">
                <h2>Available Endpoints:</h2>
                <div class="endpoint">
                    <strong>GET</strong> <code>/</code> - Home page
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/health</code> - Health check
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/notes</code> - Get all notes
                </div>
                <div class="endpoint">
                    <strong>POST</strong> <code>/notes</code> - Add new note (JSON: {"title": "...", "content": "..."})
                </div>
            </div>
        </div>
    </body>
    </html>
    """


@app.route('/health')
def health():
    """Health check endpoint."""
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({
            'status': 'healthy',
            'database': 'connected'
        }), 200
    else:
        return jsonify({
            'status': 'unhealthy',
            'database': 'disconnected'
        }), 503


@app.route('/notes', methods=['GET'])
def get_notes():
    """Get all notes from database."""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 503
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM notes ORDER BY created_at DESC;')
        notes = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({'notes': notes}), 200
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500


@app.route('/notes', methods=['POST'])
def add_note():
    """Add new note to database."""
    data = request.get_json()
    
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required'}), 400
    
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 503
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            'INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING *;',
            (data['title'], data['content'])
        )
        new_note = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'note': new_note}), 201
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)