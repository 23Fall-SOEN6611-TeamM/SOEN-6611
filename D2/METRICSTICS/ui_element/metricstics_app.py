import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from ui_element.enter_data_dialog import EnterDataDialog
from ui_element.generate_data_dialog import GenerateDataDialog
from ui_element.left_frame import LeftFrame
from ui_element.login_dialog import LoginDialog
from ui_element.middle_frame import MiddleFrame
from ui_element.right_frame import RightFrame
from statistic_tool.calculator import Calculator
from PIL import Image, ImageTk
import os
import glob


class MetricsticsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = None
        self.withdraw()
        authenticated = self.login()
        if authenticated:
            self.right_frame = None
            self.title("METRICSTICS - v1.0")
            self.geometry("1000x600")
            self.configure(bg='LightBlue')

            self.logo_image = Image.open("images/logo.png")
            self.logo_image = self.logo_image.resize((25, 25), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(self.logo_image)

            copyright_label = tk.Label(self, image=self.logo,
                                       text="© 2023 Concordia University \n23 Fall SOEN 6611 - Team M. All rights "
                                            "reserved.",
                                       compound="left", font=('Arial', 8), padx=5, pady=5, bg='LightBlue')
            copyright_label.pack(side="bottom", pady=(0, 0))

            self.csv_file = None
            self.calculator = Calculator()

            self.menu_bar = tk.Menu(self)
            self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="LightBlue")
            self.file_menu.add_command(label="Enter Data", command=self.enter_data)
            self.file_menu.add_command(label="Generate Data", command=self.generate_data)
            self.file_menu.add_command(label="CSV File", command=self.load_csv)
            self.menu_bar.add_cascade(label="Import Data", menu=self.file_menu)

            # 创建Tool菜单
            self.tool_menu = tk.Menu(self.menu_bar, tearoff=0, bg="LightBlue")
            self.tool_menu.add_command(label="Load Pre-data", command=self.load_pre_data)
            self.tool_menu.add_command(label="Export Data", command=self.export_data)
            self.menu_bar.add_cascade(label="Tool", menu=self.tool_menu)

            self.config(menu=self.menu_bar, bg='LightBlue')

            self.main_frame = tk.Frame(self, bg='LightBlue')
            self.main_frame.pack(fill="both", expand=True)

            self.left_frame = LeftFrame(self.main_frame)
            self.left_frame.pack(side="left", fill="y", expand=True, padx=(10, 0), pady=10)
            self.main_frame.grid_columnconfigure(0, weight=1)

            self.middle_frame = MiddleFrame(self.main_frame, self, self.calculator, self.right_frame)
            self.middle_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            self.main_frame.grid_columnconfigure(1, weight=2)

            self.right_frame = RightFrame(self.main_frame)
            self.right_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)
            self.main_frame.grid_columnconfigure(2, weight=3)

            self.update_idletasks()
            self.update_frames()
            self.bind("<Configure>", self.update_frames)
            self.deiconify()
        else:
            self.destroy()

    def login(self):
        dialog = LoginDialog(self, "Login")
        if dialog.authenticated:
            self.username = dialog.get_username()
        return dialog.authenticated

    def update_frames(self, event=None):
        new_width = max(self.main_frame.winfo_width(), 1)
        left_width = max(new_width * 0.1, 1)
        middle_width = max(new_width * 0.4, 1)
        right_width = max(new_width * 0.5, 1)
        self.left_frame.config(width=left_width)
        self.middle_frame.config(width=middle_width)
        self.right_frame.config(width=right_width)
        self.left_frame.update_width(left_width)

    def enter_data(self):
        try:
            dialog = EnterDataDialog(self, "Enter Data")
            if dialog.result:
                self.left_frame.set_data(dialog.result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while entering data: {str(e)}")

    def generate_data(self):
        try:
            dialog = GenerateDataDialog(self, "Generate Data", 2)
            if dialog.result:
                self.left_frame.set_data(dialog.result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while generating data: {str(e)}")

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                data = pd.read_csv(file_path, header=None)

                if not all(data[0].apply(lambda x: isinstance(x, (int, float)))):
                    messagebox.showwarning("Invalid Data",
                                           "The CSV file contains invalid data. Please make sure all values are "
                                           "integers or floats.")
                    return

                data_values = data[0].astype(float).tolist()

                if any(num < 0 or num > 1000 for num in data_values):
                    messagebox.showwarning("Invalid Data",
                                           "The CSV file contains numbers outside the valid range of 0 to 1000. "
                                           "Please make sure all values are within this range.")
                    return

                self.left_frame.set_data(data_values)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load the CSV file: {str(e)}")

    def load_pre_data(self):
        if self.username is None:
            messagebox.showwarning("Warning", "You are not logged in.")
            return

        folder_path = os.path.join('database', self.username)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        files = glob.glob(os.path.join(folder_path, '*.xlsx'))
        if not files:
            messagebox.showinfo("Info", "No previous data found.")
            return

        file_names = [os.path.basename(file) for file in files]

        def on_file_select(file_name):
            file_path = os.path.join(folder_path, file_name)
            try:
                data = pd.read_excel(file_path, sheet_name='Data')
                results = pd.read_excel(file_path, sheet_name='Results')

                self.left_frame.set_data(data.values.tolist())

                results_df = pd.read_excel(file_path, sheet_name="Results")

                results_dict = results_df.set_index('Statistic').to_dict()['Value']
                self.middle_frame.set_results(results_dict)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load the data: {str(e)}")

        select_file_dialog = tk.Toplevel(self)
        select_file_dialog.title("Select a file")
        select_file_dialog.geometry("300x200")

        listbox = tk.Listbox(select_file_dialog)
        listbox.pack(fill="both", expand=True, padx=10, pady=10)
        for file_name in file_names:
            listbox.insert("end", file_name)

        listbox.bind("<<ListboxSelect>>", lambda event: on_file_select(listbox.get(listbox.curselection())))

    def export_data(self):
        data = [item[1] for item in self.left_frame.get_data() if item[1]]

        if not data:
            tk.messagebox.showerror("Export Error", "No available data to export.")
            return

        results_data = self.middle_frame.get_results_data()

        if not results_data:
            tk.messagebox.showerror("Export Error", "No results data available to export.")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                filetypes=[("Excel files", "*.xlsx")])
        if filepath:
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                pd.Series(data, name='Data').to_frame().to_excel(writer, sheet_name='Data', index=False)
                df = pd.DataFrame(results_data, columns=['Statistic', 'Value'])
                df.to_excel(writer, sheet_name='Results', index=False)
            tk.messagebox.showinfo("Export Data", "Data exported successfully!")
