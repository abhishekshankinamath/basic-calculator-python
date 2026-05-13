import customtkinter as ctk
import sqlite3
from tkinter import messagebox

class LoginSystem:

    def __init__(self, root, open_calculator):

        self.root = root
        self.open_calculator = open_calculator

        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
        )
        """)

        self.title = ctk.CTkLabel(
            root,
            text="AI Calculator Login",
            font=("Arial", 30)
        )
        self.title.pack(pady=30)

        self.username = ctk.CTkEntry(
            root,
            placeholder_text="Username",
            width=300
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            root,
            placeholder_text="Password",
            show="*",
            width=300
        )
        self.password.pack(pady=10)

        self.login_btn = ctk.CTkButton(
            root,
            text="Login",
            command=self.login
        )
        self.login_btn.pack(pady=10)

        self.register_btn = ctk.CTkButton(
            root,
            text="Register",
            command=self.register
        )
        self.register_btn.pack(pady=10)

    def register(self):

        user = self.username.get()
        pwd = self.password.get()

        self.cursor.execute(
            "INSERT INTO users VALUES(?,?)",
            (user, pwd)
        )

        self.conn.commit()

        messagebox.showinfo(
            "Success",
            "Registration Successful"
        )

    def login(self):

        user = self.username.get()
        pwd = self.password.get()

        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (user, pwd)
        )

        result = self.cursor.fetchone()

        if result:
            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            self.open_calculator()

        else:
            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )