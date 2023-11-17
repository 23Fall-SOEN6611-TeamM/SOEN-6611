import tkinter as tk
from tkinter import ttk


class LeftFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0")

        # Add top separator
        left_separator = tk.Frame(self, height=5, bg="black")
        left_separator.pack(fill="x")

        self.loaded_data_label = tk.Label(
            self, text="Loaded Data", font=("Arial", 9, "bold")
        )
        self.loaded_data_label.pack(side="top", anchor="w", pady=(5, 0), padx=(10, 0))
        bottom_separator = tk.Frame(self, height=3, bg="#696969")
        bottom_separator.pack(fill="x")

        # Create table
        self.data_table = ttk.Treeview(self, columns=("#", "Value"), show="headings")
        self.data_table.heading("#", text="#")
        self.data_table.heading("Value", text="Value")
        self.data_table.column("#", anchor="center")
        self.data_table.column("Value", anchor="center")

        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.data_table.yview
        )
        self.data_table.configure(yscrollcommand=self.scrollbar.set)

        self.data_table.tag_configure("evenrow", background="#f0f0ff")
        self.data_table.tag_configure("oddrow", background="#ffffff")

    def update_width(self, new_width):
        try:
            scrollbar_width = 20  # Adjust if necessary
            table_width = max(int(new_width) - scrollbar_width, 1)
            col_width = max((table_width - 20) // 2, 1)
            self.data_table.column("#", width=col_width)
            self.data_table.column("Value", width=col_width)
        except ValueError:
            print("Invalid width value:", new_width)
        except Exception as e:
            print("An error occurred:", str(e))

    def get_data(self):
        data = []
        try:
            for item in self.data_table.get_children():
                values = self.data_table.item(item).get("values")
                if values is not None:
                    data.append(values)
                else:
                    print("Warning: An item in the treeview is missing 'values'")
        except Exception as e:
            print("An error occurred while getting data:", str(e))
        return data

    def set_data(self, values):
        try:
            if not values:
                self.data_table.pack_forget()
                self.scrollbar.pack_forget()
            else:
                self.data_table.pack(side="left", fill="both", expand=True)
                self.scrollbar.pack(side="right", fill="y")
                self.data_table.delete(*self.data_table.get_children())
                for index, value in enumerate(values, start=1):
                    row_tag = "evenrow" if index % 2 == 0 else "oddrow"
                    self.data_table.insert(
                        "", "end", values=(index, value), tags=(row_tag,)
                    )

        except TypeError as e:
            print("Invalid data type:", str(e))
        except Exception as e:
            print("An error occurred while setting data:", str(e))
