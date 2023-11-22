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
        return self.round_number(min_value, 2)

    def maximum(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        max_value = self.data[0]
        for value in self.data:
            if value > max_value:
                max_value = value
        return self.round_number(max_value, 2)

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
            sorted_data = self.my_sorted(self.data)
        except Exception as e:
            print("Error: An error occurred while sorting the data.")
            print("Details:", e)
            return None
        n = len(sorted_data)
        if n % 2 == 1:
            return self.round_number(sorted_data[n // 2], 2)
        else:
            mid1 = sorted_data[(n - 1) // 2]
            mid2 = sorted_data[n // 2]
            return self.round_number((mid1 + mid2) / 2, 2)

    def mean(self):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        try:
            return self.round_number(sum(self.data) / len(self.data), 2)
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
        return self.round_number(sum(self.absolute_value(x - μ) for x in self.data) / len(self.data), 2)

    def standard_deviation(self, decimal_places=2):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        μ = self.mean()
        if μ is None:
            return None
        variance = sum((x - μ) ** 2 for x in self.data) / len(self.data)
        std_dev = variance ** 0.5
        return self.round_number(std_dev, decimal_places)

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

    def round_number(self, number, ndigits=None):
        if ndigits is None:
            ndigits = 0
        elif ndigits < 0:
            raise ValueError("ndigits must be non-negative")

        # Shift the decimal point to the right by ndigits
        # So we can work with the integer part for rounding
        shift = 10 ** ndigits
        temp = number * shift

        # Get the integer and the fractional part of the number
        integer_part = int(temp)
        fractional_part = temp - integer_part

        # Check the fractional part to decide how to round the integer part
        if fractional_part >= 0.5:
            # Round up
            integer_part += 1

        # Shift the decimal point back to the original position
        return integer_part / shift

    def absolute_value(self, number):
        """
        Return the absolute value of the number given.
        """
        # Check if the number is negative
        if number < 0:
            # If the number is negative, make it positive by multiplying by -1
            return -number
        else:
            # If the number is not negative, it is already positive, so return as is
            return number

    def quicksort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]
            less = [x for x in data[1:] if x < pivot]
            greater = [x for x in data[1:] if x >= pivot]
            return self.quicksort(less) + [pivot] + self.quicksort(greater)

    def my_sorted(self, data):
        if not self.data:
            print("Error: No data available. Please input data first.")
            return None
        return self.quicksort(data)