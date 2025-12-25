import tkinter as tk
from tkinter import messagebox
from database import get_connection

def add_student():
    window = tk.Toplevel()
    window.title("Add Student")

    tk.Label(window, text="Student ID").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()

    tk.Label(window, text="Student Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    def save():
        sid = id_entry.get()
        name = name_entry.get()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (student_id, name) VALUES (%s, %s)",
            (sid, name)
        )
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student Added")
        window.destroy()

    tk.Button(window, text="Save", command=save).pack(pady=10)
