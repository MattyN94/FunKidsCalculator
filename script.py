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
    if value == int(value):
        return int(value)
    else:
        return value

def calculate(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get())

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
root.title("Maths is your friend!")

# Styling options
bg_color = "#eeffe8"
button_color = "#d3d3d3"
button_font = ("Calibri", 12)
entry_font = ("Calibri", 14)
result_font = ("Calibri", 14, "bold")
calculate_font = ("Calibri", 12, "italic")

root.configure(bg=bg_color)

entry1 = tk.Entry(root, font=entry_font)
entry1.pack(padx=10, pady=5)

entry2 = tk.Entry(root, font=entry_font)
entry2.pack(padx=10, pady=5)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(padx=10, pady=5)

add_button = tk.Button(button_frame, text="+", command=lambda: calculate("+"), font=button_font, bg=button_color)
add_button.grid(row=0, column=0, padx=5, pady=5)

subtract_button = tk.Button(button_frame, text="-", command=lambda: calculate("-"), font=button_font, bg=button_color)
subtract_button.grid(row=0, column=1, padx=5, pady=5)

multiply_button = tk.Button(button_frame, text="*", command=lambda: calculate("*"), font=button_font, bg=button_color)
multiply_button.grid(row=0, column=2, padx=5, pady=5)

divide_button = tk.Button(button_frame, text="/", command=lambda: calculate("/"), font=button_font, bg=button_color)
divide_button.grid(row=0, column=3, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate!", font=calculate_font, bg=button_color)
calculate_button.pack(padx=10, pady=5)

m_plus_button = tk.Button(root, text="M+", command=save_memory, font=button_font, bg=button_color)
m_plus_button.pack(padx=10, pady=5)

mrc_button = tk.Button(root, text="MRC", command=retrieve_memory, font=button_font, bg=button_color)
mrc_button.pack(padx=10, pady=5)

mc_button = tk.Button(root, text="MC", command=clear_memory, font=button_font, bg=button_color)
mc_button.pack(padx=10, pady=5)

result = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result, font=result_font, bg=bg_color)
result_label.pack(padx=10, pady=10)

root.mainloop()
