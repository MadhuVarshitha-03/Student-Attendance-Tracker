import tkinter as tk
from student import add_student
from attendance import mark_attendance

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.geometry("300x250")

        tk.Button(self.root, text="Add Student", command=add_student).pack(pady=10)
        tk.Button(self.root, text="Mark Attendance", command=mark_attendance).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=10)

        self.root.mainloop()
