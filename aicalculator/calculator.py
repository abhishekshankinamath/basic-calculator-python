import customtkinter as ctk
from tkinter import messagebox
import math
import sqlite3

from graph_plot import plot_graph
from voice import voice_input
from ai_solver import solve_ai

class CalculatorApp:

    def __init__(self, root):

        self.root = root
        self.expression = ""

        # DATABASE
        self.conn = sqlite3.connect("history.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
        calculation TEXT
        )
        """)

        # TITLE
        self.title = ctk.CTkLabel(
            root,
            text="AI Scientific Calculator",
            font=("Arial", 35)
        )

        self.title.pack(pady=20)

        # DISPLAY
        self.display = ctk.CTkEntry(
            root,
            width=800,
            height=70,
            font=("Arial", 30)
        )

        self.display.pack(pady=20)

        # BUTTONS
        buttons = [
            ['7','8','9','/','sqrt'],
            ['4','5','6','*','sin'],
            ['1','2','3','-','cos'],
            ['0','.','=','+','tan'],
            ['log','pow','Graph','Voice','AI'],
            ['History','Clear']
        ]

        for row in buttons:

            frame = ctk.CTkFrame(root)
            frame.pack(pady=5)

            for btn in row:

                button = ctk.CTkButton(
                    frame,
                    text=btn,
                    width=120,
                    height=60,
                    font=("Arial",20),
                    command=lambda b=btn:self.click(b)
                )

                button.pack(side="left", padx=5)

    def click(self, button):

        if button == "=":
            self.calculate()

        elif button == "Clear":
            self.expression = ""

        elif button == "sqrt":
            self.expression += "math.sqrt("

        elif button == "sin":
            self.expression += "math.sin("

        elif button == "cos":
            self.expression += "math.cos("

        elif button == "tan":
            self.expression += "math.tan("

        elif button == "log":
            self.expression += "math.log10("

        elif button == "pow":
            self.expression += "**"

        elif button == "Graph":
            plot_graph()

        elif button == "Voice":
            self.expression += voice_input()

        elif button == "AI":
            solve_ai()

        elif button == "History":
            self.show_history()

        else:
            self.expression += str(button)

        self.update_display()

    def update_display(self):

        self.display.delete(0, 'end')
        self.display.insert(0, self.expression)

    def calculate(self):

        try:

            result = eval(self.expression)

            record = f"{self.expression} = {result}"

            self.cursor.execute(
                "INSERT INTO history VALUES(?)",
                (record,)
            )

            self.conn.commit()

            self.expression = str(result)

            self.update_display()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def show_history(self):

        self.cursor.execute(
            "SELECT * FROM history"
        )

        data = self.cursor.fetchall()

        text = ""

        for item in data:
            text += item[0] + "\n"

        messagebox.showinfo(
            "History",
            text
        )