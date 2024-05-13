import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Enter password length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5)

        self.password_value = tk.Label(master, text="")
        self.password_value.grid(row=2, column=1, padx=5, pady=5)

        self.copy_button = tk.Button(master, text="Copy Password", command=self.copy_password)
        self.copy_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
        except ValueError as ve:
            self.password_value.config(text=str(ve))
            return

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation

        all_chars = lowercase + uppercase + digits + special_chars

        password = ''.join(random.choices(all_chars, k=length))
        self.password_value.config(text=password)

    def copy_password(self):
        password = self.password_value.cget("text")
        if password:
            pyperclip.copy(password)
            self.master.clipboard_append(password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
