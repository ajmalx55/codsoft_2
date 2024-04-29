import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    label_result.config(text="Result: " + str(result))

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets for numbers
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Create label for operation choice
label_operation = tk.Label(root, text="Operation:")
label_operation.grid(row=1, column=0, padx=5, pady=5)

# Create dropdown menu for operation choice
operation_var = tk.StringVar(root)
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
dropdown_operation = tk.OptionMenu(root, operation_var, *operation_choices)
dropdown_operation.grid(row=1, column=1, padx=5, pady=5)

# Create button to perform calculation
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=2, columnspan=2, padx=5, pady=5)

# Create label to display result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
