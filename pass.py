import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip  

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar()
        self.include_upper_var = tk.BooleanVar()
        self.include_lower_var = tk.BooleanVar()
        self.include_digits_var = tk.BooleanVar()
        self.include_symbols_var = tk.BooleanVar()

        self.length_var.set(12)
        self.include_upper_var.set(True)
        self.include_lower_var.set(True)
        self.include_digits_var.set(True)
        self.include_symbols_var.set(True)

        self.setup_ui()

    def setup_ui(self):
        length_label = ttk.Label(self.root, text="Password Length:")
        length_entry = ttk.Entry(self.root, textvariable=self.length_var, width=5)

        upper_check = ttk.Checkbutton(self.root, text="Uppercase", variable=self.include_upper_var)
        lower_check = ttk.Checkbutton(self.root, text="Lowercase", variable=self.include_lower_var)
        digits_check = ttk.Checkbutton(self.root, text="Digits", variable=self.include_digits_var)
        symbols_check = ttk.Checkbutton(self.root, text="Symbols", variable=self.include_symbols_var)

        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        copy_button = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)

        length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        upper_check.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        lower_check.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        digits_check.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        symbols_check.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        generate_button.grid(row=5, column=0, columnspan=2, pady=10)
        copy_button.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        upper_chars = string.ascii_uppercase if self.include_upper_var.get() else ""
        lower_chars = string.ascii_lowercase if self.include_lower_var.get() else ""
        digit_chars = string.digits if self.include_digits_var.get() else ""
        symbol_chars = string.punctuation if self.include_symbols_var.get() else ""

        all_chars = upper_chars + lower_chars + digit_chars + symbol_chars

        if not all_chars:
            messagebox.showwarning("Warning", "Please select at least one character set.")
            return

        password = ''.join(random.choice(all_chars) for _ in range(self.length_var.get()))
        messagebox.showinfo("Generated Password", password)

    def copy_to_clipboard(self):
        generated_password = pyperclip.paste()

        if generated_password:
            pyperclip.copy(generated_password)
            messagebox.showinfo("Success", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Warning", "No password to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
