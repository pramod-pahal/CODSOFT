import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3)
]

for symbol, row, column in buttons:
    button = tk.Button(root, text=symbol, padx=30, pady=20, command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=column)

calculate_button = tk.Button(root, text='Enter', padx=66, pady=20, command=calculate)
calculate_button.grid(row=5, column=1, columnspan=2)

clear_button = tk.Button(root, text='Clear', padx=66, pady=20, command=clear)
clear_button.grid(row=5, column=0)

root.mainloop()
