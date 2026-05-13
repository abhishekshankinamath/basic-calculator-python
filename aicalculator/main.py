import customtkinter as ctk
from login import LoginSystem
from calculator import CalculatorApp

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("1200x800")
root.title("AI Advanced Calculator")

def open_calculator():

    for widget in root.winfo_children():
        widget.destroy()

    CalculatorApp(root)

LoginSystem(root, open_calculator)

root.mainloop()