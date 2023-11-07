class Calculator:
    def __init__(self):
        self.data = None

    def input_data(self, data_string):
        if not data_string:
            print("Error: Input data string is empty.")
            return
        data_list = data_string.split(',')
        try:
            self.data = [float(x.strip()) for x in data_list if x.strip()]
        except ValueError as e:
            print("Error: Please make sure all the data points are valid numbers.")
            print("Details:", e)
            self.data = None
            return

    def minimum(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        min_value = self.data[0]
        for value in self.data:
            if value < min_value:
                min_value = value
        return round(min_value, 2)

    def maximum(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        max_value = self.data[0]
        for value in self.data:
            if value > max_value:
                max_value = value
        return round(max_value, 2)

    def mode(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        frequency = {}
        for value in self.data:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
        max_frequency = 0
        mode_values = []
        for key, value in frequency.items():
            if value > max_frequency:
                max_frequency = value
                mode_values = [key]
            elif value == max_frequency:
                mode_values.append(key)
        return mode_values

    def median(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        try:
            sorted_data = sorted(self.data)
        except Exception as e:
            print("Error: An error occurred while sorting the data.")
            print("Details:", e)
            return None
        n = len(sorted_data)
        if n % 2 == 1:
            return round(sorted_data[n // 2], 2)
        else:
            mid1 = sorted_data[(n - 1) // 2]
            mid2 = sorted_data[n // 2]
            return round((mid1 + mid2) / 2, 2)

    def mean(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        try:
            return round(sum(self.data) / len(self.data), 2)
        except ZeroDivisionError:
            print("Error: Division by zero occurred. This should not happen.")
            return None

    def mean_absolute_deviation(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        μ = self.mean()
        if μ is None:
            return None
        return round(sum(abs(x - μ) for x in self.data) / len(self.data), 2)

    def standard_deviation(self, decimal_places=2):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        μ = self.mean()
        if μ is None:
            return None
        variance = sum((x - μ) ** 2 for x in self.data) / len(self.data)
        std_dev = variance ** 0.5
        return round(std_dev, decimal_places)

    def descriptive_statistics(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        return {
            "Minimum Value": self.minimum(),
            "Maximum Value": self.maximum(),
            "Mode": self.mode(),
            "Median": self.median(),
            "Mean": self.mean(),
            "Mean Absolute Deviation": self.mean_absolute_deviation(),
            "Standard Deviation": self.standard_deviation()
        }
