import tkinter as tk
from tkinter import messagebox

# Operations
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            result_label.config(text="❌ Cannot divide by zero!")
        else:
            result = float(entry1.get()) / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add (+)", width=10, command=add).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Subtract (-)", width=10, command=subtract).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Multiply (*)", width=10, command=multiply).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Divide (/)", width=10, command=divide).grid(row=3, column=1, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=('Arial', 12, 'bold'))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Exit Button
tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
