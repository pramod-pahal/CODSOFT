import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = tasks.curselection()[0]
        tasks.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    confirmed = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if confirmed:
        tasks.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.grid(row=1, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear All", width=10, command=clear_tasks)
clear_button.grid(row=1, column=1, padx=5, pady=5)

tasks = tk.Listbox(root, height=15, width=50)
tasks.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
