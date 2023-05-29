import tkinter as tk
from tkinter import ttk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_button():
    entry.delete(0, tk.END)

def equal_button():
    try:
        expression = entry.get()
        if "/ 0" in expression:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Errore: Divisione per zero")
        else:
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Errore: " + str(e))

def sin_button():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Errore: " + str(e))

def cos_button():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Errore: " + str(e))

def tan_button():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Errore: " + str(e))

def left_parenthesis():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "(")

def right_parenthesis():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + ")")

def square_button():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Errore: " + str(e))

def delete_button():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def variable_button(var):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + var)

def insert_operator(operator):
    current = entry.get()
    if current.endswith(("(", "+", "-", "*", "/")):
        return
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

window = tk.Tk()
window.title("Calcolatrice Scientifica")
window.geometry("400x400")

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#222', foreground='white')
style.configure('TEntry', fieldbackground='#333', foreground='white')
style.configure('TLabel', background='#333', foreground='white')

entry = ttk.Entry(window, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

numbers = list(range(1, 10))
row = 1
col = 0
for number in numbers:
    button = ttk.Button(window, text=str(number), width=6,
                        command=lambda num=number: button_click(num))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        col = 0
        row += 1

button_zero = ttk.Button(window, text="0", width=6,
                         command=lambda: button_click(0))
button_zero.grid(row=4, column=0, padx=5, pady=5)

clear_button = ttk.Button(window, text="    🗑️", width=6,
                          command=clear_button, compound=tk.CENTER)
clear_button.grid(row=4, column=1, padx=5, pady=5)

equal_button = ttk.Button(window, text="=", width=6,
                          command=equal_button)
equal_button.grid(row=4, column=2, padx=5, pady=5)

operations = ["+", "-", "*", "/"]
row = 1
for operation in operations:
    button = ttk.Button(window, text=operation, width=6,
                        command=lambda op=operation: insert_operator(op))
    button.grid(row=row, column=3, padx=5, pady=5)
    row += 1

sin_button = ttk.Button(window, text="sin", width=6,
                        command=sin_button)
sin_button.grid(row=1, column=4, padx=5, pady=5)

cos_button = ttk.Button(window, text="cos", width=6,
                        command=cos_button)
cos_button.grid(row=2, column=4, padx=5, pady=5)

tan_button = ttk.Button(window, text="tan", width=6,
                        command=tan_button)
tan_button.grid(row=3, column=4, padx=5, pady=5)

left_parenthesis_button = ttk.Button(window, text="(", width=6,
                                     command=left_parenthesis)
left_parenthesis_button.grid(row=4, column=3, padx=5, pady=5)

right_parenthesis_button = ttk.Button(window, text=")", width=6,
                                      command=right_parenthesis)
right_parenthesis_button.grid(row=4, column=4, padx=5, pady=5)

square_button = ttk.Button(window, text="x^2", width=6,
                           command=square_button)
square_button.grid(row=5, column=0, padx=5, pady=5)

delete_button = ttk.Button(window, text="Del", width=6,
                           command=delete_button)
delete_button.grid(row=5, column=1, padx=5, pady=5)

window.mainloop()
