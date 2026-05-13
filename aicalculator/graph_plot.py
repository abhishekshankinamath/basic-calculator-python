import numpy as np
import matplotlib.pyplot as plt
from tkinter import simpledialog

def plot_graph():

    equation = simpledialog.askstring(
        "Graph",
        "Enter equation using x\nExample: x**2"
    )

    x = np.linspace(-10,10,400)

    y = eval(equation)

    plt.plot(x,y)

    plt.title(equation)

    plt.grid(True)

    plt.show()