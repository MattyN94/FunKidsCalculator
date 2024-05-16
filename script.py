import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result.set(add(num1, num2))
    elif operation == "-":
        result.set(subtract(num1, num2))
    elif operation == "*":
        result.set(multiply(num1, num2))
    elif operation == "/":
        result.set(divide(num1, num2))

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.pack()

operation_var = tk.StringVar(root)
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack()

entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
