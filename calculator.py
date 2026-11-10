import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("400x450")
root.resizable(False, False)

# Create the display
display = tk.Entry(
    root,
    font=("Arial", 20),
    justify="right",
    bd=10
)
display.pack(fill="x", padx=10, pady=10)


# Function to display clicked buttons
def button_click(value):
    display.insert(tk.END, value)


# Function to clear the display
def clear_display():
    display.delete(0, tk.END)


# Function to calculate the result
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        clear_display()
        display.insert(0, str(result))
    except ZeroDivisionError:
        clear_display()
        display.insert(0, "Cannot divide by zero")
    except Exception:
        clear_display()
        display.insert(0, "Error")


# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

button_frame = tk.Frame(root)
button_frame.pack()

# Create the button layout
for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):

        if value == "C":
            command = clear_display
        elif value == "=":
            command = calculate
        else:
            command = lambda v=value: button_click(v)

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18),
            width=4,
            height=2,
            command=command
        )

        button.grid(
            row=row_index + 1,
            column=col_index,
            padx=5,
            pady=5
        )

# Run the application
root.mainloop()

