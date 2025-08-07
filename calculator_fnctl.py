import tkinter as tk
from tkinter import ttk

# Initialize the main window
window = tk.Tk()
window.title('Calculator')
window.geometry("400x500")  # Set a window size for better layout

# Create a Style object
style = ttk.Style(window)
style.theme_use('clam')  # Use 'clam' theme for better styling control

# Configure the TButton style
style.configure('TButton',
                font=('Arial', 20, 'bold'),
                padding=10,
                relief='raised',
                background='#FFFACD',  # Light yellow background
                foreground='#000000',  # Black text
                borderwidth=2)

# Define the active state color
style.map('TButton',
          background=[('active', '#E6E6FA')],  # Light blue background when active '#B3E5FC'
          relief=[('pressed', 'sunken')])

# Entry field
entry = tk.Entry(window, width=20, borderwidth=5, bg='#E3F2FD', fg='#5A4ACD',
                  font='Arial 30 bold', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='we')

# Function to handle adding number to the entry
def add_btn(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(num))

# Function to handle clearing the entry
def clear():
    entry.delete(0, tk.END)

# Function to handle operations (+, -, *, /)
def operation(op):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + op)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Number buttons (1-9)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, num in enumerate(numbers):
    row = index // 3 + 1
    col = index % 3
    ttk.Button(window, text=str(num), style='TButton',
               command=lambda n=num: add_btn(n)).grid(
        row=row, column=col, sticky='nsew', padx=5, pady=5)

# Zero button
ttk.Button(window, text='0', style='TButton', command=lambda: add_btn(0)).grid(
    row=4, column=1, sticky='nsew', padx=5, pady=5)

# Operation buttons (+, *, -, /)
ttk.Button(window, text='+', style='TButton', command=lambda: operation('+')).grid(
    row=1, column=3, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='*', style='TButton', command=lambda: operation('*')).grid(
    row=2, column=3, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='-', style='TButton', command=lambda: operation('-')).grid(
    row=3, column=3, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='/', style='TButton', command=lambda: operation('/')).grid(
    row=4, column=3, sticky='nsew', padx=5, pady=5)

# Equals button
ttk.Button(window, text='=', style='TButton', command=calculate).grid(
    row=4, column=2, sticky='nsew', padx=5, pady=5)

# Clear button
ttk.Button(window, text='C', style='TButton', command=clear).grid(
    row=5, column=0, sticky='nsew', padx=5, pady=5)

# Adjust grid weights for resizing
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
