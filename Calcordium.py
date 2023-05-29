import tkinter as tk
from tkinter import ttk
import math

class CalcordiumCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Caldordium")
        self.window.geometry("400x400")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#222', foreground='white')
        style.configure('TEntry', fieldbackground='#333', foreground='white')
        style.configure('TLabel', background='#333', foreground='white')

        self.entry = ttk.Entry(self.window, width=20, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'log'],
            ['1', '2', '3', '-', 'ln'],
            ['0', '.', '=', '+', 'C'],
            ['[', ']', '{', '}', '^2'],
            ['(', ')', '%', '!', 'mod']
        ]

        row = 1
        col = 0
        for button_row in buttons:
            for button_text in button_row:
                button = ttk.Button(self.window, text=button_text, width=6,
                                    command=lambda text=button_text: self.button_click(text))
                button.grid(row=row, column=col, padx=5, pady=5)
                col += 1
            row += 1
            col = 0

        self.window.mainloop()

    def button_click(self, value):
        if value == '=':
            self.equal_button()
        elif value == 'sqrt':
            self.sqrt_button()
        elif value == 'log':
            self.log_button()
        elif value == '^2':
            self.square_button()
        elif value == 'C':
            self.clear_button()
        elif value == 'ln':
            self.ln_button()
        elif value == 'mod':
            self.modulo_button()
        elif value == '!':
            self.fattoriale_button()
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current + str(value))

    def equal_button(self):
        try:
            expression = self.entry.get()
            if "/ 0" in expression:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Errore: Divisione per zero")
            else:
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))

    def sqrt_button(self):
        try:
            value = float(self.entry.get())
            result = math.sqrt(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))

    def log_button(self):
        try:
            value = float(self.entry.get())
            result = math.log10(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))

    def square_button(self):
        try:
            value = float(self.entry.get())
            result = value ** 2
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))

    def clear_button(self):
        self.entry.delete(0, tk.END)

    def ln_button(self):
        try:
            value = float(self.entry.get())
            result = math.log(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))

    def modulo_button(self):
        try:
            expression = self.entry.get()
            if "/ 0" in expression:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Errore: Divisione per zero")
            else:
                result = eval(expression) % 1
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))

    def fattoriale_button(self):
        try:
            value = int(self.entry.get())
            result = math.factorial(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Errore: " + str(e))


if __name__ == "__main__":
    app = CalcordiumCalculator()
