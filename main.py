# Import necessary modules from the Tkinter library
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Create the main window
window = tk.Tk()
window.title('Calculator')

# Create a frame within the window with a blue background and padding
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()

# Create an entry widget for displaying the input and output
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

# Define functions for button clicks and calculations
def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        # Evaluate the expression in the entry and display the result
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        # Show an error message in case of a syntax error
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    # Clear the entry widget
    entry.delete(0, tk.END)

# Create number buttons (0-9) with associated click actions
for i in range(1, 10):
    button = tk.Button(master=frame, text=str(i), padx=15, pady=5, width=3, command=lambda i=i: myclick(i))
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3, pady=2)

# Create button for zero (0)
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

# Create operation buttons (+, -, *, /) with associated click actions
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button_operator = tk.Button(master=frame, text=operator, padx=15, pady=5, width=3, command=lambda operator=operator: myclick(operator))
    button_operator.grid(row=5, column=i, pady=2)

# Create clear button with an associated click action
button_clear = tk.Button(master=frame, text="clear", padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

# Create equal button with an associated click action
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

# Start the Tkinter main event loop
window.mainloop()
