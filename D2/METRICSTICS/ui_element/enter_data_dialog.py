import tkinter as tk
from tkinter import simpledialog, messagebox


class EnterDataDialog(simpledialog.Dialog):
    def __init__(self, parent, title="Enter Data"):
        super().__init__(parent, title)

    def body(self, frame):
        self.label = tk.Label(frame, text="Enter data (comma separated):")
        self.label.pack(padx=10, pady=10)

        self.text_frame = tk.Frame(frame)
        self.text_frame.pack(padx=10, pady=10, fill='both', expand=True)

        self.text = tk.Text(self.text_frame, width=40, height=5, wrap='word')
        self.text.pack(side='left', fill='both', expand=True)

        self.scrollbar = tk.Scrollbar(self.text_frame, command=self.text.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.text.configure(yscrollcommand=self.scrollbar.set)
        return self.text

    def validate(self):
        data = self.text.get("1.0", tk.END).strip()
        if not data:
            messagebox.showwarning("Invalid Input", "Data field cannot be empty.")
            return 0
        try:
            self.result = [float(x.strip()) for x in data.split(',') if x.strip()]
        except ValueError:
            messagebox.showwarning("Invalid Input", "Data must be a list of numbers separated by commas.")
            return 0

        # Check if the numbers are within the range of 0 to 1000
        if any(num < 0 or num > 1000 for num in self.result):
            messagebox.showwarning("Invalid Input", "Numbers must be between 0 and 1000.")
            return 0

        return 1


