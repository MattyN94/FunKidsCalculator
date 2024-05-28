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

def format_result(value):
    # Format the result to show without decimal if it's an integer
    if value == int(value):
        return int(value)
    else:
        return value

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result_value = add(num1, num2)
    elif operation == "-":
        result_value = subtract(num1, num2)
    elif operation == "*":
        result_value = multiply(num1, num2)
    elif operation == "/":
        result_value = divide(num1, num2)

    result.set(format_result(result_value))

def save_memory():
    with open("memory.txt", "w") as file:
        file.write(str(result.get()))

def retrieve_memory():
    try:
        with open("memory.txt", "r") as file:
            value = file.read()
            entry1.delete(0, tk.END)
            entry1.insert(0, value)
    except FileNotFoundError:
        result.set("No memory found")

def clear_memory():
    with open("memory.txt", "w") as file:
        file.write("")

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

m_plus_button = tk.Button(root, text="M+", command=save_memory)
m_plus_button.pack()

mrc_button = tk.Button(root, text="MRC", command=retrieve_memory)
mrc_button.pack()

mc_button = tk.Button(root, text="MC", command=clear_memory)
mc_button.pack()

result = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
