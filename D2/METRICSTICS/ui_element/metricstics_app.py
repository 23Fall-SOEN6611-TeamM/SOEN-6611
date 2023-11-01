import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from ui_element.enter_data_dialog import EnterDataDialog
from ui_element.generate_data_dialog import GenerateDataDialog
from ui_element.left_frame import LeftFrame
from ui_element.middle_frame import MiddleFrame
from ui_element.right_frame import RightFrame
from statistic_tool.calculator import Calculator
from PIL import Image, ImageTk
import platform

class MetricsticsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # if platform.system() == "Darwin":  # macOS
        #     self.attributes('-zoomed', True)
        # else:
        #     self.state('zoomed')

        self.right_frame = None
        self.title("METRICSTICS - v1.0")
        self.geometry("1000x600")
        self.configure(bg='LightBlue')

        self.logo_image = Image.open("images/logo.png")
        self.logo_image = self.logo_image.resize((25, 25), Image.Resampling.LANCZOS)  # 调整图片大小
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
        # self.file_menu.add_command(label="CSV File", command=lambda: load_csv(self))
        self.file_menu.add_command(label="CSV File", command=self.load_csv)

        self.menu_bar.add_cascade(label="Data Source", menu=self.file_menu)
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

