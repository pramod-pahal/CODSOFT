import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_frame = tk.Frame(root)
password_frame.pack(pady=5)

password_label = tk.Label(password_frame, text="Password:")
password_label.pack(side=tk.LEFT)

password_entry = tk.Entry(password_frame, width=40)
password_entry.pack(side=tk.LEFT)

root.mainloop()
