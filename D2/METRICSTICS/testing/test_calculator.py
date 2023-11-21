import random
from statistic_tool.calculator import Calculator


# function to generate randomly distributed values between 0 and 1000
def generate_random_data(size, min_value=0, max_value=1000):
    return ", ".join(str(random.uniform(min_value, max_value)) for _ in range(size))


# Test cases for minimum function data count - 50,000
def test_minimum_valid_data():
    data = generate_random_data(50000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.minimum() == round(min(map(float, data.split(", "))), 2)


def test_minimum_no_data():
    calculator = Calculator()
    assert calculator.minimum() is None


# data count - 50,000
def test_minimum_negative_values():
    data = generate_random_data(50000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.minimum() == round(min(map(float, data.split(", "))), 2)


# data count - 50,000
def test_minimum_duplicate_values():
    data = generate_random_data(50000) + ", " + generate_random_data(500)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.minimum() == round(min(map(float, data.split(", "))), 2)


# Test cases for maximum function # data count - 50,000
def test_maximum_valid_data():
    data = generate_random_data(50000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.maximum() == round(max(map(float, data.split(", "))), 2)


def test_maximum_no_data():
    calculator = Calculator()
    assert calculator.maximum() is None


# data count - 50,000
def test_maximum_negative_values():
    data = generate_random_data(50000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.maximum() == round(max(map(float, data.split(", "))), 2)


# data count - 10,000
def test_maximum_duplicate_values():
    data = generate_random_data(10000) + ", " + generate_random_data(500)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.maximum() == round(max(map(float, data.split(", "))), 2)


# Test cases for mode function # data count - 20,000
def test_mode_valid_data_single_mode():
    data = generate_random_data(20000) + ", 5, 5, 5, 5, 5"
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mode() == [5.0]


# data count - 20,000
def test_mode_valid_data_multiple_modes():
    data = generate_random_data(20000) + ", 5, 5, 5, 6, 6, 6"
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mode() == [5.0, 6.0]


def test_mode_no_data():
    calculator = Calculator()
    assert calculator.mode() is None


# data count - 20,000
def test_mode_all_unique_values():
    data = generate_random_data(20000)
    calculator = Calculator()
    calculator.input_data(data)
    expected_mode = sorted(list(set(map(float, data.split(", ")))))
    assert sorted(calculator.mode()) == expected_mode

# data count - 9999
def test_median_valid_data_even():
    data = generate_random_data(9999) + ", 10000"
    calculator = Calculator()
    calculator.input_data(data)
    sorted_data = sorted(map(float, data.split(", ")))
    mid = len(sorted_data) // 2
    assert calculator.median() == round(
        (sorted_data[mid - 1] + sorted_data[mid]) / 2, 2
    )


def test_median_no_data():
    calculator = Calculator()
    assert calculator.median() is None


# data count - 50,000
def test_median_duplicate_values():
    data = generate_random_data(50000) + ", " + generate_random_data(500)
    calculator = Calculator()
    calculator.input_data(data)
    sorted_data = sorted(map(float, data.split(", ")))
    mid = len(sorted_data) // 2
    assert calculator.median() == round(
        (sorted_data[mid - 1] + sorted_data[mid]) / 2, 2
    )


# Test cases for mean function # data count - 50,000
def test_mean_valid_data():
    data = generate_random_data(50000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mean() == round(
        sum(map(float, data.split(", "))) / len(data.split(", ")), 2
    )


def test_mean_no_data():
    calculator = Calculator()
    assert calculator.mean() is None


# data count - 100,000
def test_mean_negative_values():
    data = generate_random_data(100000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mean() == round(
        sum(map(float, data.split(", "))) / len(data.split(", ")), 2
    )


# data count - 100,000
def test_mean_decimal_values():
    data = generate_random_data(100000, 0, 100)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mean() == round(
        sum(map(float, data.split(", "))) / len(data.split(", ")), 2
    )


# Test cases for mean_absolute_deviation function # data count - 100,000
def test_mean_absolute_deviation_valid_data():
    data = generate_random_data(100000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    assert calculator.mean_absolute_deviation() == round(
        sum(abs(float(x) - mean) for x in data.split(", ")) / len(data.split(", ")), 2
    )


def test_mean_absolute_deviation_no_data():
    calculator = Calculator()
    assert calculator.mean_absolute_deviation() is None


# data count - 100,000
def test_mean_absolute_deviation_negative_values():
    data = generate_random_data(100000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    assert calculator.mean_absolute_deviation() == round(
        sum(abs(float(x) - mean) for x in data.split(", ")) / len(data.split(", ")), 2
    )


# data count - 100,000
def test_mean_absolute_deviation_decimal_values():
    data = generate_random_data(100000, 0, 100)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    assert calculator.mean_absolute_deviation() == round(
        sum(abs(float(x) - mean) for x in data.split(", ")) / len(data.split(", ")), 2
    )


# Test cases for standard_deviation function # data count - 100,000
def test_standard_deviation_valid_data():
    data = generate_random_data(100000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    variance = sum((float(x) - mean) ** 2 for x in data.split(", ")) / len(
        data.split(", ")
    )
    assert calculator.standard_deviation() == round(variance**0.5, 2)


def test_standard_deviation_no_data():
    calculator = Calculator()
    assert calculator.standard_deviation() is None


# data count - 100,000
def test_standard_deviation_negative_values():
    data = generate_random_data(100000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    variance = sum((float(x) - mean) ** 2 for x in data.split(", ")) / len(
        data.split(", ")
    )
    assert calculator.standard_deviation() == round(variance**0.5, 2)


# data count - 100,000
def test_standard_deviation_decimal_values():
    data = generate_random_data(100000, 0, 100)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    variance = sum((float(x) - mean) ** 2 for x in data.split(", ")) / len(
        data.split(", ")
    )
    assert calculator.standard_deviation() == round(variance**0.5, 2)
