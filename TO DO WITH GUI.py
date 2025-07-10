import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TODO_FILE = "todo.txt"

# ===== File Handling =====
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ===== GUI Functionality =====
def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append("[ ] " + task)
        save_tasks(tasks)
        refresh_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Warning", "Task cannot be empty!")

def mark_done():
    try:
        index = listbox.curselection()[0]
        if tasks[index].startswith("[x]"):
            messagebox.showinfo("Info", "Task already marked as done.")
        else:
            tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            refresh_listbox()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to mark as done.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        removed = tasks.pop(index)
        save_tasks(tasks)
        refresh_listbox()
        messagebox.showinfo("Deleted", f"🗑️ Removed: {removed}")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

# ===== UI Setup =====
root = tk.Tk()
root.title("To-Do List")

# Load tasks
tasks = load_tasks()

# Input field
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Buttons
tk.Button(root, text="Add Task", width=15, command=add_task).grid(row=0, column=2, padx=5)
tk.Button(root, text="Mark as Done", width=15, command=mark_done).grid(row=1, column=0, pady=5)
tk.Button(root, text="Delete Task", width=15, command=delete_task).grid(row=1, column=1, pady=5)
tk.Button(root, text="Exit", width=15, command=root.quit, bg="red", fg="white").grid(row=1, column=2, pady=5)

# Task list
listbox = tk.Listbox(root, width=60, height=10, selectmode=tk.SINGLE)
listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

refresh_listbox()

root.mainloop()
