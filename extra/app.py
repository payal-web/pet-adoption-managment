from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="btsarmy2008",  # 🔑 Put your actual password here
        database="pet_adoption"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets WHERE status = "Available"')
    pets = cursor.fetchall()
    conn.close()
    return render_template('index.html', pets=pets)

@app.route('/adopt/<int:pet_id>')
def adopt(pet_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE pets SET status = "Adopted" WHERE pet_id = %s', (pet_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
