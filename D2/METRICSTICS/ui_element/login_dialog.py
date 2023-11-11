import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd


class LoginDialog(simpledialog.Dialog):
    def __init__(self, parent, title):
        self.username = ""
        self.password = ""
        self.authenticated = False
        self.user_data = pd.read_excel('database/users.xlsx', sheet_name='Sheet1')
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x200")
        self.resizable(False, False)

        top_frame = tk.Frame(master)
        top_frame.pack(side="top", fill="both", expand=True)

        tk.Label(top_frame, text="Welcome To METRICSTICS", fg='#B22222', font=("Lucida Handwriting", 13, "bold")).pack(pady=20)

        input_frame = tk.Frame(master)
        input_frame.pack(side="top", fill="both", expand=True, padx=20, pady=5)

        tk.Label(input_frame, text="Username:").grid(row=0, column=0)
        tk.Label(input_frame, text="Password:").grid(row=1, column=0)

        self.e1 = tk.Entry(input_frame)
        self.e2 = tk.Entry(input_frame, show="*")

        self.e1.grid(row=0, column=1, pady=5)
        self.e2.grid(row=1, column=1, pady=5)

        master.bind('<Return>', lambda event: self.ok())

        return self.e1

    def apply(self):
        self.username = self.e1.get()
        self.password = self.e2.get()
        self.user_data['Password'] = self.user_data['Password'].astype(str)
        if ((self.user_data['Username'] == self.username) & (self.user_data['Password'] == self.password)).any():
            self.authenticated = True
        else:
            messagebox.showerror("Error", "Invalid username or password")
            self.e1.delete(0, tk.END)
            self.e2.delete(0, tk.END)
            self.e1.focus_set()
            self.authenticated = False

    def ok(self, event=None):
        self.apply()
        if self.authenticated:
            super().ok()

    def get_username(self):
        return self.username if self.authenticated else None
