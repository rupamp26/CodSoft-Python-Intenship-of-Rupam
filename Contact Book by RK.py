import tkinter as tk
from tkinter import ttk, messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.phone})"

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.contacts = []

        # Create Treeview to display contacts
        self.tree = ttk.Treeview(master, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.pack(pady=10)

        # Create buttons
        add_button = ttk.Button(master, text="Add Contact", command=self.show_add_contact_window)
        add_button.pack(pady=5)

        update_button = ttk.Button(master, text="Update Contact", command=self.show_update_contact_window)
        update_button.pack(pady=5)

        delete_button = ttk.Button(master, text="Delete Contact", command=self.delete_contact)
        delete_button.pack(pady=5)

        view_button = ttk.Button(master, text="View Contacts", command=self.view_contacts)
        view_button.pack(pady=5)

    def show_add_contact_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Contact")

        name_label = ttk.Label(add_window, text="Name:")
        name_label.pack(pady=5)
        name_entry = ttk.Entry(add_window)
        name_entry.pack(pady=5)

        phone_label = ttk.Label(add_window, text="Phone:")
        phone_label.pack(pady=5)
        phone_entry = ttk.Entry(add_window)
        phone_entry.pack(pady=5)

        email_label = ttk.Label(add_window, text="Email:")
        email_label.pack(pady=5)
        email_entry = ttk.Entry(add_window)
        email_entry.pack(pady=5)

        address_label = ttk.Label(add_window, text="Address:")
        address_label.pack(pady=5)
        address_entry = ttk.Entry(add_window)
        address_entry.pack(pady=5)

        def add_contact():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            address = address_entry.get()

            if name and phone:
                contact = Contact(name, phone, email, address)
                self.contacts.append(contact)
                self.tree.insert("", "end", values=(contact.name, contact.phone, contact.email, contact.address))
                messagebox.showinfo("Success", f"{name} has been added to your contact book.")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter a name and phone number.")

        add_button = ttk.Button(add_window, text="Add Contact", command=add_contact)
        add_button.pack(pady=5)

    def show_update_contact_window(self):
        selected = self.tree.focus()
        if selected:
            name = self.tree.item(selected, "values")[0]
            update_window = tk.Toplevel(self.master)
            update_window.title("Update Contact")

            name_label = ttk.Label(update_window, text="Name:")
            name_label.pack(pady=5)
            name_entry = ttk.Entry(update_window)
            name_entry.insert(0, name)
            name_entry.pack(pady=5)

            phone_label = ttk.Label(update_window, text="Phone:")
            phone_label.pack(pady=5)
            phone_entry = ttk.Entry(update_window)
            phone_entry.insert(0, self.tree.item(selected, "values")[1])
            phone_entry.pack(pady=5)

            email_label = ttk.Label(update_window, text="Email:")
            email_label.pack(pady=5)
            email_entry = ttk.Entry(update_window)
            email_entry.insert(0, self.tree.item(selected, "values")[2])
            email_entry.pack(pady=5)

            address_label = ttk.Label(update_window, text="Address:")
            address_label.pack(pady=5)
            address_entry = ttk.Entry(update_window)
            address_entry.insert(0, self.tree.item(selected, "values")[3])
            address_entry.pack(pady=5)

            def update_contact():
                new_name = name_entry.get()
                new_phone = phone_entry.get()
                new_email = email_entry.get()
                new_address = address_entry.get()

                if new_name and new_phone:
                    for contact in self.contacts:
                        if contact.name == name:
                            contact.name = new_name
                            contact.phone = new_phone
                            contact.email = new_email
                            contact.address = new_address
                            self.tree.item(selected, values=(new_name, new_phone, new_email, new_address))
                            messagebox.showinfo("Success", f"{name}'s contact has been updated.")
                            update_window.destroy()
                            break
                else:
                    messagebox.showerror("Error", "Please enter a name and phone number.")

            update_button = ttk.Button(update_window, text="Update Contact", command=update_contact)
            update_button.pack(pady=5)
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected = self.tree.focus()
        if selected:
            name = self.tree.item(selected, "values")[0]
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {name}'s contact?")
            if confirm:
                for contact in self.contacts:
                    if contact.name == name:
                        self.contacts.remove(contact)
                        self.tree.delete(selected)
                        messagebox.showinfo("Success", f"{name}'s contact has been deleted.")
                        break
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact Book", "Your contact book is empty.")
        else:
            view_window = tk.Toplevel(self.master)
            view_window.title("View Contacts")

            view_tree = ttk.Treeview(view_window, columns=("Name", "Phone", "Email", "Address"), show="headings")
            view_tree.heading("Name", text="Name")
            view_tree.heading("Phone", text="Phone")
            view_tree.heading("Email", text="Email")
            view_tree.heading("Address", text="Address")
            view_tree.pack(pady=10)

            for contact in self.contacts:
                view_tree.insert("", "end", values=(contact.name, contact.phone, contact.email, contact.address))

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()