
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="btsarmy2008",  # Add your MySQL password if needed
        database="pet_adoption"  # Ensure your database name is correct
    )

# Home page route: Get Started page
@app.route('/')
def home():
    return render_template('home.html')  # Render the Get Started page

@app.route('/pets')
def index():
    sort_by = request.args.get('sort_by', 'name')  # Default sort
    allowed_sorts = ['name', 'age', 'breed', 'gender']
    if sort_by not in allowed_sorts:
        sort_by = 'name'

    query = f"SELECT pet_id, name, breed, age, gender, status, image FROM pets WHERE status = 'available' ORDER BY {sort_by}"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    pets = cursor.fetchall()
    conn.close()

    return render_template('index.html', pets=pets)


# Adopt a pet route
@app.route('/adopt/<int:pet_id>', methods=['GET', 'POST'])
def adopt(pet_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Form data from the adoption page
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        try:
            # Insert the adopter info into the database
            cursor.execute('INSERT INTO adopter (name, phone, email) VALUES (%s, %s, %s)', (name, phone, email))
            adopter_id = cursor.lastrowid  # Get the last inserted adopter ID

            # Update pet status to 'Adopted'
            cursor.execute('UPDATE pets SET status = "Adopted" WHERE pet_id = %s', (pet_id,))

            # Insert adoption record into the adoption table
            cursor.execute('INSERT INTO adoption (pet_id, adopter_id, adoption_date) VALUES (%s, %s, NOW())',
                           (pet_id, adopter_id))

            conn.commit()  # Commit the changes
            conn.close()
            return redirect(url_for('success'))  # Redirect to success page after adoption
        except Exception as e:
            conn.rollback()  # Rollback on error
            conn.close()
            return f"Error during adoption: {str(e)}"  # Show the error
    else:
        # Fetch pet details for adoption form
        cursor.execute('SELECT * FROM pets WHERE pet_id = %s', (pet_id,))
        pet = cursor.fetchone()
        conn.close()
        return render_template('adopt.html', pet=pet)

# Success route after adoption
@app.route('/success')
def success():
    return render_template('success.html')  # Render success page

if __name__ == '__main__':
    app.run(debug=True)
