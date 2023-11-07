import tkinter as tk
from tkinter import simpledialog, messagebox
import random


class GenerateDataDialog(simpledialog.Dialog):
    def __init__(self, parent, title="Generate Data", decimal_places=2):
        self.decimal_places = decimal_places
        super().__init__(parent, title)

    def body(self, frame):
        self.label = tk.Label(frame, text="Enter the number of data points to generate (greater than 0):")
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(frame)
        self.entry.pack(padx=10, pady=10)
        return self.entry

    def validate(self):
        data = self.entry.get().strip()
        if not data.isdigit() or int(data) <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a valid number greater than 0.")
            return 0
        return 1

    def apply(self):
        num_points_str = self.entry.get().strip()
        try:
            num_points = int(num_points_str)
        except ValueError:
            messagebox.showerror("Error", "An unexpected error occurred when converting the number of data points.")
            self.result = None
            return

        try:
            self.result = [str(round(random.uniform(0, 1000), self.decimal_places)) for _ in range(num_points)]
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred when generating the data: {str(e)}")
            self.result = None
