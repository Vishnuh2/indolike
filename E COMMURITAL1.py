import tkinter as tk
from tkinter import messagebox

# Sample product database
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Smartphone", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 1500},
    {"id": 4, "name": "Keyboard", "price": 700},
    {"id": 5, "name": "Mouse", "price": 500},
]

cart = []

# Add to cart
def add_to_cart(product, quantity_entry):
    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            raise ValueError
        cart.append({"product": product, "quantity": quantity})
        messagebox.showinfo("Added", f"✅ Added {quantity} x {product['name']} to cart.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "⚠️ Enter a valid quantity (positive number).")

# View cart contents
def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("🛒 Your Cart")
    cart_window.geometry("400x300")

    if not cart:
        tk.Label(cart_window, text="Your cart is empty.").pack(pady=20)
        return

    total = 0
    for item in cart:
        name = item["product"]["name"]
        price = item["product"]["price"]
        quantity = item["quantity"]
        item_total = price * quantity
        total += item_total
        tk.Label(cart_window, text=f"{name} x {quantity} = ₹{item_total}").pack(anchor='w')

    tk.Label(cart_window, text=f"\n💰 Total: ₹{total}", font=("Arial", 12, "bold")).pack(pady=10)

# Checkout
def checkout():
    if not cart:
        messagebox.showinfo("Cart Empty", "🛒 Your cart is empty.")
        return

    result = messagebox.askyesno("Confirm Checkout", "Proceed to checkout?")
    if result:
        cart.clear()
        messagebox.showinfo("Success", "🎉 Purchase successful! Thank you for shopping.")

# GUI Setup
root = tk.Tk()
root.title("🛒 Simple E-Commerce System")
root.geometry("500x500")

tk.Label(root, text="📦 Available Products", font=("Arial", 14, "bold")).pack(pady=10)

for p in products:
    frame = tk.Frame(root, pady=5)
    frame.pack(fill="x")

    info = tk.Label(frame, text=f"{p['name']} - ₹{p['price']}", width=30, anchor="w")
    info.pack(side="left", padx=10)

    quantity_entry = tk.Entry(frame, width=5)
    quantity_entry.insert(0, "1")
    quantity_entry.pack(side="left")

    add_button = tk.Button(frame, text="Add to Cart", command=lambda p=p, q=quantity_entry: add_to_cart(p, q))
    add_button.pack(side="left", padx=10)

# Action buttons
tk.Button(root, text="🛍️ View Cart", command=view_cart, width=20).pack(pady=10)
tk.Button(root, text="💳 Checkout", command=checkout, width=20).pack(pady=10)
tk.Button(root, text="🚪 Exit", command=root.quit, width=20).pack(pady=10)

root.mainloop()
