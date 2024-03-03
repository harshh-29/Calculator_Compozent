import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "Cannot divide by zero")
        return None

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Responsive Calculator")

        # Configure color scheme
        bg_color = '#E0E0E0'  # Light grey background
        fg_color = '#FFFFFF'  # Dark blue text
        button_bg_color = '#99CC00'  # Light green for numeric buttons
        operator_bg_color = '#006633'  # Dark green for arithmetic operators

        # Entry widget to display input and results
        self.entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, insertwidth=4, justify='right', bg=bg_color, fg=fg_color)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button grid
        buttons = [
            ('7', 1, 0, button_bg_color), ('8', 1, 1, button_bg_color), ('9', 1, 2, button_bg_color), ('/', 1, 3, operator_bg_color),
            ('4', 2, 0, button_bg_color), ('5', 2, 1, button_bg_color), ('6', 2, 2, button_bg_color), ('*', 2, 3, operator_bg_color),
            ('1', 3, 0, button_bg_color), ('2', 3, 1, button_bg_color), ('3', 3, 2, button_bg_color), ('-', 3, 3, operator_bg_color),
            ('0', 4, 0, button_bg_color), ('C', 4, 1, '#33CC33'), ('=', 4, 2, '#003366'), ('+', 4, 3, operator_bg_color)
        ]

        for (text, row, column, color) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg=color, fg=fg_color, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

        # Configure row and column weights for responsiveness
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current_text = self.entry.get()

        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
