import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password(length=6):
    alphabet =  string.digits 
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)

def create_calculator():
    def update_display(value):
        current_text = display_var.get()
        if current_text == "0":
            display_var.set(value)
        else:
            display_var.set(current_text + value)

    def clear_display():
        display_var.set("0")

    def calculate_result():
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")

    def check_password():
        entered_password = password_entry.get()
        if entered_password == password:  # Replace with your desired password
            calculator_frame.pack()  # Show calculator if password is correct
            password_label.pack_forget()  # Hide password label and entry
            password_entry.pack_forget()
        else:
            messagebox.showerror("Incorrect Password", "Incorrect password. Please try again.")

    # Create the main window
    parent = tk.Tk()
    parent.title("Password Protected Calculator")

    # Password Entry Section
    password_label = tk.Label(parent, text="Enter Password:")
    password_label.pack(pady=10)

    password_entry = tk.Entry(parent, show="*")
    password_entry.pack(pady=5)

    check_button = tk.Button(parent, text="Enter", command=check_password)
    check_button.pack(pady=10)

    # Calculator Section (Initially hidden)
    calculator_frame = tk.Frame(parent)

    # Create and place the display label
    display_var = tk.StringVar()
    display_var.set("0")

    display_label = tk.Label(calculator_frame, textvariable=display_var, width=20, font=("Arial", 24), anchor="e", bg="lightgray", fg="brown", padx=28, pady=28)
    display_label.grid(row=0, column=0, columnspan=4)

    # Define button layout
    button_layout = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ]


    # Create and place the calculator buttons
    for (text, row, col) in button_layout:
        if text == "C":
            button = tk.Button(calculator_frame, text=text, padx=40, pady=40, font=("Arial", 20), bg="gray", command=clear_display)
        elif text == "=":
            button = tk.Button(calculator_frame, text=text, padx=38, pady=40, font=("Arial", 20), bg="gray", command=calculate_result)
        else:
            button = tk.Button(calculator_frame, text=text, padx=45, pady=45, font=("Arial", 20), bg="gray", command=lambda t=text: update_display(t))
        button.grid(row=row, column=col)
        


    # Pack calculator frame initially hidden
    calculator_frame.pack_forget()

    # Run the main loop
    parent.mainloop()

# Call the function to create the calculator
create_calculator()


