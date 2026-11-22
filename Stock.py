

import tkinter as tk
from tkinter import ttk, messagebox

# Stock Prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 190
}

total_investment = 0

# Main Window
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("800x550")
root.configure(bg="#eaf2f8")

# Heading
title = tk.Label(
    root,
    text="STOCK PORTFOLIO TRACKER",
    font=("Arial", 22, "bold"),
    bg="#1a5276",
    fg="white",
    pady=15
)
title.pack(fill="x")

# Input Frame
frame = tk.Frame(root, bg="#eaf2f8")
frame.pack(pady=20)

tk.Label(frame, text="Stock Name:", font=("Arial", 12),
         bg="#eaf2f8").grid(row=0, column=0, padx=10, pady=10)

stock_entry = tk.Entry(frame, font=("Arial", 12), width=15)
stock_entry.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Quantity:", font=("Arial", 12),
         bg="#eaf2f8").grid(row=0, column=2, padx=10)

quantity_entry = tk.Entry(frame, font=("Arial", 12), width=15)
quantity_entry.grid(row=0, column=3, padx=10)

# Portfolio Table
columns = ("Stock", "Price", "Quantity", "Investment")

table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor="center")

table.pack(pady=20, padx=20, fill="x")

# Total Investment
total_label = tk.Label(
    root,
    text="Total Investment: ₹0",
    font=("Arial", 16, "bold"),
    bg="#eaf2f8",
    fg="#1a5276"
)
total_label.pack(pady=10)

# Add Stock Function
def add_stock():
    global total_investment

    stock_name = stock_entry.get().upper().strip()

    try:
        quantity = int(quantity_entry.get())

        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be greater than 0")
            return

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity")
        return

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        table.insert(
            "",
            "end",
            values=(stock_name, price, quantity, investment)
        )

        total_label.config(
            text=f"Total Investment: ₹{total_investment}"
        )

        stock_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Error", "Stock not found!")

# Clear Function
def clear_portfolio():
    global total_investment

    for item in table.get_children():
        table.delete(item)

    total_investment = 0
    total_label.config(text="Total Investment: ₹0")

# Buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Add Stock",
    font=("Arial", 12, "bold"),
    bg="#2874a6",
    fg="white",
    command=add_stock,
    width=15
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear Portfolio",
    font=("Arial", 12, "bold"),
    bg="#c0392b",
    fg="white",
    command=clear_portfolio,
    width=15
).grid(row=0, column=1, padx=10)

# Footer
tk.Label(
    root,
    text="Developed by Atharva Manekar",
    font=("Arial", 10),
    bg="#eaf2f8",
    fg="gray"
).pack(side="bottom", pady=10)

# Run Application
root.mainloop()
