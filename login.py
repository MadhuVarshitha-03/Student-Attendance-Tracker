import tkinter as tk
from tkinter import messagebox
from database import get_connection

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Attendance - Login")
        self.root.geometry("300x200")

        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Success", "Login Successful")
            self.root.destroy()
            import dashboard
            dashboard.Dashboard()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
