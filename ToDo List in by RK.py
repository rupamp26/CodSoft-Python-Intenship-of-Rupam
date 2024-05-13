import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.tasks_listbox = tk.Listbox(master, width=50)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=5, pady=5)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, f"{len(self.tasks)}. {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.tasks_listbox.delete(index)
            self.update_task_numbers()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[index] = new_task
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"{index + 1}. {new_task}")
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            self.tasks_listbox.insert(tk.END, f"{index}. {task}")

    def update_task_numbers(self):
        self.tasks_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.tasks_listbox.insert(tk.END, f"{index}. {task}")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
