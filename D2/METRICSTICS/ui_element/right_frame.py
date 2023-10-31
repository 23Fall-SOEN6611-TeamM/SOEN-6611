import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk


def handle_exception(func):
    try:
        func()
    except TypeError as e:
        messagebox.showerror("Type Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


class RightFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='LightBlue')
        plt.style.use('seaborn-v0_8-whitegrid')

        right_separator = tk.Frame(self, height=5, bg="Royal Blue")
        right_separator.pack(fill="x")

        self.label = tk.Label(self, text="Data Visualization", font=("Helvetica", 12, "bold"), bg='LightBlue')
        self.label.pack(side="top", pady=(10, 0), anchor='center')

        plt.rcParams['figure.facecolor'] = '#f0f0f0'
        # self.figure = plt.Figure(figsize=(5, 4), dpi=100)

        self.figure, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(padx=10, pady=10, fill='both', expand=True)
        self.set_background("images/chart.png")

    def set_background(self, image_path):
        image = Image.open(image_path)
        image_array = np.asarray(image)
        self.ax.axis('off')  # 关闭坐标轴
        self.ax.imshow(image_array, aspect='auto')
        self.canvas.draw()

    def clear(self):
        self.figure.clf()

    def draw_bar_chart(self, data, stats):
        def plot():
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("data must be a list of integers or floats")
            if not isinstance(stats, dict):
                raise TypeError("stats must be a dictionary")

            ax = self.figure.add_subplot(111)
            x_values = list(range(1, len(data) + 1))  # 从1开始
            bars = ax.bar(x_values, data)
            min_val = stats["Minimum Value"]
            max_val = stats["Maximum Value"]
            mean_val = stats["Mean"]
            mad_val = stats["Mean Absolute Deviation"]
            std_dev = stats["Standard Deviation"]

            if min_val in data:
                ax.plot(x_values[data.index(min_val)], min_val, 'ro')
                ax.annotate("m", (x_values[data.index(min_val)], min_val), textcoords="offset points", xytext=(0, 10),
                            ha='center')

            if max_val in data:
                ax.plot(x_values[data.index(max_val)], max_val, 'ro')
                ax.annotate("M", (x_values[data.index(max_val)], max_val), textcoords="offset points", xytext=(0, 10),
                            ha='center')

            ax.plot([min(x_values), max(x_values)], [mean_val, mean_val], 'r--')
            ax.annotate("μ", (max(x_values), mean_val), textcoords="offset points", xytext=(0, 10), ha='right')

            ax.plot([min(x_values), max(x_values)], [mad_val, mad_val], 'r--')
            ax.annotate("MAD", (max(x_values), mad_val), textcoords="offset points", xytext=(0, 10), ha='right')

            ax.plot([min(x_values), max(x_values)], [std_dev, std_dev], 'r--')
            ax.annotate("σ", (max(x_values), std_dev), textcoords="offset points", xytext=(0, 10), ha='right')

            ax.set_xticks(x_values)
            ax.set_xticklabels([str(x) for x in x_values])
            ax.set_title("Bar Chart", loc='center', fontsize=12, pad=20, color='steelblue', fontweight='bold')
            self.canvas.draw()

        handle_exception(plot)

    def draw_histogram(self, data, stats):
        def plot():
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("data must be a list of integers or floats")
            if not isinstance(stats, dict):
                raise TypeError("stats must be a dictionary")

            ax = self.figure.add_subplot(111)
            n, bins, patches = ax.hist(data, bins='auto', edgecolor='black')

            min_val = stats.get("Minimum Value", None)
            max_val = stats.get("Maximum Value", None)
            mean_val = stats.get("Mean", None)

            if min_val is not None:
                ax.plot([min_val, min_val], [0, max(n)], 'r--')
                ax.annotate("Min", (min_val, max(n)), textcoords="offset points", xytext=(0, 10), ha='left')

            if max_val is not None:
                ax.plot([max_val, max_val], [0, max(n)], 'r--')
                ax.annotate("Max", (max_val, max(n)), textcoords="offset points", xytext=(0, 10), ha='right')

            if mean_val is not None:
                ax.plot([mean_val, mean_val], [0, max(n)], 'r--')
                ax.annotate("Mean", (mean_val, max(n)), textcoords="offset points", xytext=(0, 10), ha='center')
            ax.set_title("Histogram", loc='center', fontsize=12, pad=20, color='steelblue', fontweight='bold')

            self.canvas.draw()

        handle_exception(plot)

    def draw_box_plot(self, data, stats):
        def plot():
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("data must be a list of integers or floats")
            if not isinstance(stats, dict):
                raise TypeError("stats must be a dictionary")

            ax = self.figure.add_subplot(111)
            boxplot = ax.boxplot(data, vert=False)

            min_val = stats.get("Minimum Value", None)
            max_val = stats.get("Maximum Value", None)
            mean_val = stats.get("Mean", None)

            if min_val is not None:
                ax.plot(min_val, 1, 'ro')
                ax.annotate("Min", (min_val, 1), textcoords="offset points", xytext=(-20, 0), ha='center')

            if max_val is not None:
                ax.plot(max_val, 1, 'ro')
                ax.annotate("Max", (max_val, 1), textcoords="offset points", xytext=(20, 0), ha='center')

            if mean_val is not None:
                ax.plot(mean_val, 1, 'ro')
                ax.annotate("Mean", (mean_val, 1), textcoords="offset points", xytext=(0, 20), ha='center')
            ax.set_title("Box Plot", loc='center', fontsize=12, pad=20, color='steelblue', fontweight='bold')
            self.canvas.draw()

        handle_exception(plot)

    def draw_dot_plot(self, data, stats):
        def plot():
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("data must be a list of integers or floats")
            if not isinstance(stats, dict):
                raise TypeError("stats must be a dictionary")

            ax = self.figure.add_subplot(111)
            ax.plot(data, 'o', markersize=5)

            min_val = stats.get("Minimum Value", None)
            max_val = stats.get("Maximum Value", None)
            mean_val = stats.get("Mean", None)
            mad_val = stats.get("Mean Absolute Deviation", None)
            std_dev = stats.get("Standard Deviation", None)

            def mark_point(value, label, x_offset=0):
                if value is not None:
                    closest_index = min(range(len(data)), key=lambda i: abs(data[i] - value))
                    ax.plot(closest_index + 1, data[closest_index], 'ro')
                    ax.annotate(label, (closest_index + 1, data[closest_index]), textcoords="offset points",
                                xytext=(x_offset, 10), ha='center')

            mark_point(min_val, 'm', -10)
            mark_point(max_val, 'M', 10)
            mark_point(mean_val, 'μ')
            mark_point(mad_val, 'MAD')
            mark_point(std_dev, 'σ')
            ax.set_title("Dot Plot", loc='center', fontsize=12, pad=20, color='steelblue', fontweight='bold')
            self.canvas.draw()

        handle_exception(plot)

    def draw_line_chart(self, data, stats):
        def plot():
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("data must be a list of integers or floats")
            if not isinstance(stats, dict):
                raise TypeError("stats must be a dictionary")

            ax = self.figure.add_subplot(111)
            x_values = range(len(data))
            ax.plot(x_values, data, marker='o', linestyle='-')

            min_val = stats.get("Minimum Value", None)
            max_val = stats.get("Maximum Value", None)
            mean_val = stats.get("Mean", None)
            mad_val = stats.get("Mean Absolute Deviation", None)
            std_dev = stats.get("Standard Deviation", None)

            def mark_point(value, label, y_offset=10, x_offset=0):
                if value is not None:
                    closest_index = min(range(len(data)), key=lambda i: abs(data[i] - value))
                    ax.plot(closest_index, data[closest_index], 'ro')
                    ax.annotate(label, (closest_index, data[closest_index]), textcoords="offset points",
                                xytext=(x_offset, y_offset), ha='center')

            mark_point(min_val, 'm', y_offset=20, x_offset=-10)
            mark_point(max_val, 'M', y_offset=20, x_offset=10)
            mark_point(mean_val, 'μ')
            mark_point(mad_val, 'MAD', y_offset=-20)
            mark_point(std_dev, 'σ', y_offset=-20)

            ax.set_xticks(x_values)
            ax.set_xticklabels([str(x) for x in x_values])
            ax.set_title("Line Chart", loc='center', fontsize=12, pad=20, color='steelblue', fontweight='bold')
            self.canvas.draw()

        handle_exception(plot)

    def draw_violin_plot(self, data, stats):
        def plot():
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("data must be a list of integers or floats")
            if not isinstance(stats, dict):
                raise TypeError("stats must be a dictionary")
            if len(data) == 0:
                raise ValueError("data cannot be an empty list")

            ax = self.figure.add_subplot(111)
            data_reshaped = np.array(data).reshape(-1, 1)
            ax.violinplot(data_reshaped)

            min_val = stats.get("Minimum Value", None)
            max_val = stats.get("Maximum Value", None)
            mean_val = stats.get("Mean", None)
            mad_val = stats.get("Mean Absolute Deviation", None)
            std_dev = stats.get("Standard Deviation", None)

            def mark_point(value, label, x_position):
                if value is not None:
                    ax.plot(x_position, value, 'ro')
                    ax.annotate(label, (x_position, value), textcoords="offset points", xytext=(0, 10), ha='center')

            mark_point(min_val, 'm', 1)
            mark_point(max_val, 'M', 1)
            mark_point(mean_val, 'μ', 1)
            mark_point(mad_val, 'MAD', 1)
            mark_point(std_dev, 'σ', 1)

            ax.set_xticks([1])
            ax.set_xticklabels(['Data'])
            ax.set_title("Violin Plot", loc='center', fontsize=12, pad=20, color='steelblue', fontweight='bold')
            self.canvas.draw()

        handle_exception(plot)

