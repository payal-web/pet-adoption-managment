# 🐾 Pet Adoption Management System

A web-based pet adoption platform built using **Flask** and **MySQL** that allows users to browse available pets and submit adoption requests.

---

## 🚀 Features

- **Home Page** – A welcoming "Get Started" landing page
- **Browse Pets** – View all available pets with details like name, breed, age, gender, and photo
- **Sort Pets** – Filter/sort pets by name, age, breed, or gender
- **Adopt a Pet** – Fill out an adoption form with your name, phone, and email
- **Auto Status Update** – Pet status automatically changes to "Adopted" after submission
- **Success Page** – Confirmation page after successful adoption

---

## 🛠️ Tech Stack

| Layer     | Technology            |
|-----------|-----------------------|
| Backend   | Python, Flask         |
| Database  | MySQL                 |
| Frontend  | HTML, CSS (Jinja2 templates) |
| ORM/DB    | mysql-connector-python |

---

## 📁 Project Structure

Pet_adoption_managment/
│
├── app.py                  # Main Flask application
├── sql                     # SQL schema/setup file
├── static/
│   ├── style.css           # Main stylesheet
│   ├── home.css            # Home page styles
│   └── images/             # Pet images (dogs, cats, rabbit, parrot)
└── templates/
├── home.html           # Landing page
├── index.html          # Browse available pets
├── adopt.html          # Adoption form
└── success.html        # Adoption success page

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/payal-web/pet-adoption-managment.git
cd pet-adoption-managment
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install flask mysql-connector-python
```

### 4. Setup MySQL Database
- Create a database named `pet_adoption`
- Run the SQL file to create tables:
```sql
CREATE TABLE pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    breed VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    status VARCHAR(20) DEFAULT 'available',
    image VARCHAR(200)
);

CREATE TABLE adopter (
    adopter_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE adoption (
    adoption_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    adopter_id INT,
    adoption_date DATETIME
);
```

### 5. Update DB credentials in `app.py`
```python
host="localhost"
user="root"
password="your_password"
database="pet_adoption"
```

### 6. Run the app
```bash
python app.py
```
Visit: `http://127.0.0.1:5000`

---

## 📸 Pages Overview

- `/` → Home / Get Started
- `/pets` → Browse available pets
- `/adopt/<pet_id>` → Adoption form for a specific pet
- `/success` → Adoption success confirmation
