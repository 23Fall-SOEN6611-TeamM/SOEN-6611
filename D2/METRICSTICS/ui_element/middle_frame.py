import tkinter as tk
from tkinter import PhotoImage


class MiddleFrame(tk.Frame):
    def __init__(self, parent, app, calculator, right_frame):
        super().__init__(parent, bg='LightBlue')
        self.app = app
        self.calculator = calculator
        self.right_frame = right_frame

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
        data = [item[1] for item in self.app.left_frame.get_data() if item[1]]
        if not data:
            tk.messagebox.showerror("Calculation Error", "No data available. Please enter data first.")
            return

        try:
            data = [float(item) for item in data]
            data_string = ','.join(map(str, data))
            self.calculator.input_data(data_string)
            results = self.calculator.descriptive_statistics()

            self.results_text.config(state=tk.NORMAL)  # Set the text widget to normal (editable) state
            self.results_text.delete(1.0, tk.END)
            for key, value in results.items():
                self.results_text.insert(tk.END, f"{key}: {value}\n")
            self.results_text.config(state=tk.DISABLED)  # Set the text widget back to disabled (non-editable) state

            selected_graph = self.selected_graph_type.get()
            self.generate_graphs(data, selected_graph, results)
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", f"Error converting data to float: {str(e)}")
        except Exception as e:
            tk.messagebox.showerror("Calculation Error", f"An error occurred: {str(e)}")

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
