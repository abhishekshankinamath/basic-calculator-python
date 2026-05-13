from sympy import symbols, Eq, solve
from tkinter import simpledialog, messagebox

def solve_ai():

    x = symbols('x')

    equation = simpledialog.askstring(
        "AI Solver",
        "Example:\n2*x+5=15"
    )

    left, right = equation.split('=')

    eq = Eq(eval(left), eval(right))

    result = solve(eq, x)

    messagebox.showinfo(
        "Answer",
        f"x = {result}"
    )