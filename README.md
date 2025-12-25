# Student-Attendance-Tracker
📚 Student Attendance Tracker

A desktop-based Student Attendance Management System developed using Python, Tkinter, and MySQL.
This application allows secure login, student record management, and attendance tracking with persistent database storage.

🚀 Features

🔐 Secure Login System

👨‍🎓 Add and Manage Student Records

📅 Mark Attendance (Present)

🗄️ MySQL Database Integration

🖥️ User-friendly Desktop GUI using Tkinter

✅ Data Integrity using Foreign Keys

🛠️ Tech Stack

Programming Language: Python 3.x

GUI Framework: Tkinter

Database: MySQL

Database Connector: mysql-connector-python

Version Control: Git & GitHub

📂 Project Structure
Student_Attendance_Tracker/
│
├── main.py            # Entry point of the application
├── login.py           # Login GUI
├── dashboard.py       # Dashboard screen
├── student.py         # Add student functionality
├── attendance.py      # Attendance marking
├── database.py        # MySQL connection
├── test_db.py         # Database connection test
├── README.md
├── .gitignore
└── venv/              # Virtual environment (ignored in Git)

⚙️ Prerequisites

Ensure the following are installed:

Python 3.10 or later

MySQL Server 8.0

Git

MySQL Workbench (optional)

🗄️ Database Setup
1️⃣ Create Database
CREATE DATABASE attendance_db;
USE attendance_db;

2️⃣ Create Tables
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    status VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

3️⃣ Insert Default Login User
INSERT INTO users (username, password)
VALUES ('admin', 'admin123');

🧪 Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/MadhuVarshitha-03/Student-Attendance-Tracker.git
cd Student_Attendance_Tracker

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate

4️⃣ Install Dependencies
pip install mysql-connector-python

🔌 Configure Database Connection

Edit database.py:

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="attendance_user",   # or root
        password="YOUR_PASSWORD",
        database="attendance_db"
    )

▶️ Run the Application
python main.py

🔑 Login Credentials
Username: admin
Password: admin123

✅ How It Works

User logs in via Tkinter GUI

Dashboard allows:

Adding students

Marking attendance

Attendance is stored in MySQL

Foreign key constraints ensure valid student data

📌 Common Issues & Fixes

Foreign key error: Add student before marking attendance

Module not found: Activate virtual environment

Access denied: Check MySQL username/password

📈 Future Enhancements

🔐 Password hashing

📊 View attendance history

📤 Export attendance to Excel

🗓️ Prevent duplicate attendance per day

🎨 Improved UI design

🎯 Resume Description

Developed a desktop-based Student Attendance Tracker using Python, Tkinter, and MySQL. Implemented secure authentication, student management, and attendance tracking with relational database integration.

🤝 Contribution

Contributions are welcome!
Feel free to fork the repository and submit a pull request.
