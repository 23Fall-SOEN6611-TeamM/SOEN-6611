import queue
import threading
import tkinter as tk
from tkinter import PhotoImage, messagebox
import pandas as pd
import os
import datetime
import time

class MiddleFrame(tk.Frame):
    def __init__(self, parent, app, calculator, right_frame):
        super().__init__(parent, bg='LightBlue')
        self.app = app
        self.calculator = calculator
        self.right_frame = right_frame
        self.last_saved_data = None
        self.after(100, self.process_queue)
        self.update_queue = queue.Queue()
        self.task_running = False

        orange_line = tk.Frame(self, bg="#B22222", height=5)
        orange_line.pack(fill='x', side='top')

        self.calculate_button = tk.Button(self, text="Analyze", command=self.calculate,
                                          width=18, font=('Arial', 15, 'bold'), bg='#B22222', fg='white')
        self.calculate_button.pack(pady=10)

        self.graph_label = tk.Label(self, text="Chart / Graph:", anchor='w', font=('Arial', 9, 'bold'), bg='LightBlue')
        self.graph_label.pack(fill='x')

        self.selected_graph_type = tk.StringVar(value="Bar Chart")

        self.graph_frame = tk.Frame(self, bg='LightBlue')
        self.graph_frame.pack()

        self.graph_types = ["Bar Chart", "Box Plot", "Histogram", "Dot Plot", "Line Chart", "Violin Plot"]
        for i, graph_type in enumerate(self.graph_types):
            row = i // 3
            column = i % 3
            radio = tk.Radiobutton(self.graph_frame, text=graph_type, variable=self.selected_graph_type,
                                   value=graph_type, bg='LightBlue')
            radio.grid(row=row, column=column, sticky='w')

        self.results_frame = tk.Frame(self, bg='LightBlue')
        self.results_frame.pack(fill='both', expand=True)

        self.results_label = tk.Label(self.results_frame, text="Results:", font=('Arial', 9, 'bold'),
                                      anchor='w', bg='LightBlue')
        self.results_label.pack(side='top', pady=(10, 0), anchor='w')

        self.results_text = tk.Text(self.results_frame, height=20, wrap='word', state=tk.DISABLED, bg='#f0f0f0')
        self.results_text.pack(side='left', pady=(0, 10), fill='both', expand=True)

        self.bg_image = PhotoImage(file='images/math.png')
        self.results_text.image_create(tk.END, image=self.bg_image)
        self.results_scroll = tk.Scrollbar(self.results_frame, orient='vertical', command=self.results_text.yview)
        self.results_text.config(yscrollcommand=self.results_scroll.set)
        self.results_scroll.pack(side='left', fill='y')

    def calculate(self):
        if self.task_running:
            threading.Thread(target=self.show_notification).start()
        self.task_running = True
        threading.Thread(target=self.calculate_in_thread).start()

    def show_notification(self):
        messagebox.showinfo("Notification",
                            "A/Some task(s) is(are) currently running. You still can analyze current data, "
                            "but the page will fresh and show the results based on the job queue, "
                            "you can check all the results from Tool -> Load Pre-data.")

    def calculate_in_thread(self):
        self.task_running = True
        data = [item[1] for item in self.app.left_frame.get_data() if item[1]]
        if not data:
            self.after(0, lambda: tk.messagebox.showerror("Calculation Error",
                                                          "No data available. Please enter data first."))
            self.task_running = False
            return

        try:
            # time.sleep(8)
            data = [float(item) for item in data]
            data_string = ','.join(map(str, data))
            self.calculator.input_data(data_string)
            results = self.calculator.descriptive_statistics()

            if results is not None:
                self.save_results_to_excel(data, results)

                def set_results_with_data(data=data, results=results):
                    self.set_results(results)

                def generate_graphs_with_data(data=data, results=results):
                    selected_graph = self.selected_graph_type.get()
                    self.generate_graphs(data, selected_graph, results)

                self.update_queue.put((data, set_results_with_data))
                self.update_queue.put((data, generate_graphs_with_data))

        except ValueError as e:
            self.after(0, lambda: tk.messagebox.showerror("Calculation Error",
                                                          f"Error converting data to float: {str(e)}"))
        except Exception as e:
            self.after(0, lambda error=e: self.show_error_msg(error))
        finally:
            self.task_running = False

    def show_error_msg(self, error):
        tk.messagebox.showerror("Calculation Error", f"An error occurred: {str(error)}")

    def process_queue(self):
        try:
            while True:
                data, task = self.update_queue.get_nowait()
                task()
                self.app.left_frame.set_data(data)
        except queue.Empty:
            pass
        self.after(100, self.process_queue)

    def save_results_to_excel(self, data, results):
        if results is None:
            print("Error: No results to save.")
            return

        if self.last_saved_data == data:
            return
        self.last_saved_data = data

        database_folder = 'database'
        if not os.path.exists(database_folder):
            os.makedirs(database_folder)

        user_folder = os.path.join(database_folder, self.app.username)

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"{self.app.username}_{now}.xlsx"
        file_path = os.path.join(user_folder, filename)

        counter = 1
        while os.path.exists(file_path):
            filename = f"{self.app.username}_{now}_{counter}.xlsx"
            file_path = os.path.join(user_folder, filename)
            counter += 1
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            pd.Series(data, name='Data').to_frame().to_excel(writer, sheet_name='Data', index=False)

            df = pd.DataFrame(list(results.items()), columns=["Statistic", "Value"])
            df.to_excel(writer, sheet_name='Results', index=False)
        # print(f"Results and data saved to {file_path}")

    def generate_graphs(self, data, selected_graph, stats):
        self.app.right_frame.clear()
        if selected_graph == "Bar Chart":
            self.app.right_frame.draw_bar_chart(data, stats)
        if selected_graph == "Box Plot":
            self.app.right_frame.draw_box_plot(data, stats)
        if selected_graph == "Histogram":
            self.app.right_frame.draw_histogram(data, stats)
        if selected_graph == "Dot Plot":
            self.app.right_frame.draw_dot_plot(data, stats)
        if selected_graph == "Line Chart":
            self.app.right_frame.draw_line_chart(data, stats)
        if selected_graph == "Violin Plot":
            self.app.right_frame.draw_violin_plot(data, stats)

    def set_results(self, results):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        for key, value in results.items():
            self.results_text.insert(tk.END, f"{key}: {value}\n")
        self.results_text.config(state=tk.DISABLED)

    def get_results_data(self):
        raw_text = self.results_text.get("1.0", tk.END).strip()
        if not raw_text:
            return None

        lines = raw_text.split("\n")
        results_data = []
        for line in lines:
            key, value_str = line.split(": ")
            try:
                value = float(value_str)
            except ValueError:
                try:
                    value = [float(v) for v in value_str.strip("[]").split(",")]
                except:
                    continue
            results_data.append((key, value))

        return results_data

