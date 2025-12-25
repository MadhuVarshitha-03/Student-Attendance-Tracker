import tkinter as tk
from tkinter import messagebox
from database import get_connection

def mark_attendance():
    window = tk.Toplevel()
    window.title("Mark Attendance")

    tk.Label(window, text="Student ID").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()

    def mark():
        sid = id_entry.get()

        conn = get_connection()
        cursor = conn.cursor()

        # Check if student exists
        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (sid,)
        )

        if cursor.fetchone() is None:
            messagebox.showerror(
                "Error",
                "Student not found. Please add student first."
            )
            conn.close()
            return

        cursor.execute(
            "INSERT INTO attendance (student_id, date, status) "
            "VALUES (%s, CURDATE(), 'Present')",
            (sid,)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Attendance Marked")
        window.destroy()

    tk.Button(window, text="Mark Present", command=mark).pack(pady=10)
