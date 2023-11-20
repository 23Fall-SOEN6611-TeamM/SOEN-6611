# import pytest
# from statistic_tool.calculator import Calculator


# # Test cases for minimum function
# def test_minimum_valid_data():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2")
#     assert calculator.minimum() == 1.0


# def test_minimum_no_data():
#     calculator = Calculator()
#     assert calculator.minimum() is None


# def test_minimum_negative_values():
#     calculator = Calculator()
#     calculator.input_data("-3, -1, -4, -1, -5, -9, -2")
#     assert calculator.minimum() == -9.0


# def test_minimum_duplicate_values():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2, 1")
#     assert calculator.minimum() == 1.0


# # Test cases for maximum function
# def test_maximum_valid_data():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2")
#     assert calculator.maximum() == 9.0


# def test_maximum_no_data():
#     calculator = Calculator()
#     assert calculator.maximum() is None


# def test_maximum_negative_values():
#     calculator = Calculator()
#     calculator.input_data("-3, -1, -4, -1, -5, -9, -2")
#     assert calculator.maximum() == -1.0


# def test_maximum_duplicate_values():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2, 5")
#     assert calculator.maximum() == 9.0


# # Test cases for mode function
# def test_mode_valid_data_single_mode():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2, 5, 6, 5")
#     assert calculator.mode() == [5.0]


# def test_mode_valid_data_multiple_modes():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2, 5, 6, 5, 6")
#     assert calculator.mode() == [5.0]


# def test_mode_no_data():
#     calculator = Calculator()
#     assert calculator.mode() is None


# def test_mode_all_unique_values():
#     calculator = Calculator()
#     calculator.input_data("1, 2, 3, 4, 5")
#     assert calculator.mode() == [1, 2, 3, 4, 5]


# # Test cases for median function
# def test_median_valid_data_odd():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2")
#     assert calculator.median() == 3.0


# def test_median_valid_data_even():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2, 6")
#     assert calculator.median() == 3.5


# def test_median_no_data():
#     calculator = Calculator()
#     assert calculator.median() is None


# def test_median_duplicate_values():
#     calculator = Calculator()
#     calculator.input_data("3, 1, 4, 1, 5, 9, 2, 6, 2, 6")
#     assert calculator.median() == 3.5


# # Test cases for mean function
# def test_mean_valid_data():
#     calculator = Calculator()
#     calculator.input_data("1, 2, 3, 4, 5")
#     assert calculator.mean() == 3.0


# def test_mean_no_data():
#     calculator = Calculator()
#     assert calculator.mean() is None


# def test_mean_negative_values():
#     calculator = Calculator()
#     calculator.input_data("-1, -2, -3, -4, -5")
#     assert calculator.mean() == -3.0


# def test_mean_decimal_values():
#     calculator = Calculator()
#     calculator.input_data("1.5, 2.5, 3.5, 4.5, 5.5")
#     assert calculator.mean() == 3.5


# # Test cases for mean_absolute_deviation function
# def test_mean_absolute_deviation_valid_data():
#     calculator = Calculator()
#     calculator.input_data("1, 2, 3, 4, 5")
#     assert calculator.mean_absolute_deviation() == 1.2


# def test_mean_absolute_deviation_no_data():
#     calculator = Calculator()
#     assert calculator.mean_absolute_deviation() is None


# def test_mean_absolute_deviation_negative_values():
#     calculator = Calculator()
#     calculator.input_data("-1, -2, -3, -4, -5")
#     assert calculator.mean_absolute_deviation() == 1.2


# def test_mean_absolute_deviation_decimal_values():
#     calculator = Calculator()
#     calculator.input_data("1.5, 2.5, 3.5, 4.5, 5.5")
#     assert calculator.mean_absolute_deviation() == 1.2


# # Test cases for standard_deviation function
# def test_standard_deviation_valid_data():
#     calculator = Calculator()
#     calculator.input_data("1, 2, 3, 4, 5")
#     assert calculator.standard_deviation() == 1.41  # Rounded to two decimal places


# def test_standard_deviation_no_data():
#     calculator = Calculator()
#     assert calculator.standard_deviation() is None


# def test_standard_deviation_negative_values():
#     calculator = Calculator()
#     calculator.input_data("-1, -2, -3, -4, -5")
#     assert calculator.standard_deviation() == 1.41  # Rounded to two decimal places


# def test_standard_deviation_decimal_values():
#     calculator = Calculator()
#     calculator.input_data("1.5, 2.5, 3.5, 4.5, 5.5")
#     assert calculator.standard_deviation() == 1.41  # Rounded to two decimal places


import random
from statistic_tool.calculator import Calculator


# function to generate randomly distributed values between 0 and 1000
def generate_random_data(size, min_value=0, max_value=1000):
    return ", ".join(str(random.uniform(min_value, max_value)) for _ in range(size))


# Test cases for minimum function
def test_minimum_valid_data():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.minimum() == round(min(map(float, data.split(", "))), 2)


def test_minimum_no_data():
    calculator = Calculator()
    assert calculator.minimum() is None


def test_minimum_negative_values():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.minimum() == round(min(map(float, data.split(", "))), 2)


def test_minimum_duplicate_values():
    data = generate_random_data(1000) + ", " + generate_random_data(500)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.minimum() == round(min(map(float, data.split(", "))), 2)


# Test cases for maximum function
def test_maximum_valid_data():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.maximum() == round(max(map(float, data.split(", "))), 2)


def test_maximum_no_data():
    calculator = Calculator()
    assert calculator.maximum() is None


def test_maximum_negative_values():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.maximum() == round(max(map(float, data.split(", "))), 2)


def test_maximum_duplicate_values():
    data = generate_random_data(1000) + ", " + generate_random_data(500)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.maximum() == round(max(map(float, data.split(", "))), 2)


# Test cases for mode function
def test_mode_valid_data_single_mode():
    data = generate_random_data(1000) + ", 5, 5, 5, 5, 5"
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mode() == [5.0]


def test_mode_valid_data_multiple_modes():
    data = generate_random_data(1000) + ", 5, 5, 5, 6, 6, 6"
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mode() == [5.0, 6.0]


def test_mode_no_data():
    calculator = Calculator()
    assert calculator.mode() is None


def test_mode_all_unique_values():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mode() == sorted(list(set(map(float, data.split(", ")))))


# Test cases for median function
def test_median_valid_data_odd():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    sorted_data = sorted(map(float, data.split(", ")))
    assert calculator.median() == round(sorted_data[len(sorted_data) // 2], 2)


def test_median_valid_data_even():
    data = generate_random_data(999) + ", 1000"
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


def test_median_duplicate_values():
    data = generate_random_data(1000) + ", " + generate_random_data(500)
    calculator = Calculator()
    calculator.input_data(data)
    sorted_data = sorted(map(float, data.split(", ")))
    mid = len(sorted_data) // 2
    assert calculator.median() == round(
        (sorted_data[mid - 1] + sorted_data[mid]) / 2, 2
    )


# Test cases for mean function
def test_mean_valid_data():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mean() == round(
        sum(map(float, data.split(", "))) / len(data.split(", ")), 2
    )


def test_mean_no_data():
    calculator = Calculator()
    assert calculator.mean() is None


def test_mean_negative_values():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mean() == round(
        sum(map(float, data.split(", "))) / len(data.split(", ")), 2
    )


def test_mean_decimal_values():
    data = generate_random_data(1000, 0, 100)
    calculator = Calculator()
    calculator.input_data(data)
    assert calculator.mean() == round(
        sum(map(float, data.split(", "))) / len(data.split(", ")), 2
    )


# Test cases for mean_absolute_deviation function
def test_mean_absolute_deviation_valid_data():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    assert calculator.mean_absolute_deviation() == round(
        sum(abs(float(x) - mean) for x in data.split(", ")) / len(data.split(", ")), 2
    )


def test_mean_absolute_deviation_no_data():
    calculator = Calculator()
    assert calculator.mean_absolute_deviation() is None


def test_mean_absolute_deviation_negative_values():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    assert calculator.mean_absolute_deviation() == round(
        sum(abs(float(x) - mean) for x in data.split(", ")) / len(data.split(", ")), 2
    )


def test_mean_absolute_deviation_decimal_values():
    data = generate_random_data(1000, 0, 100)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    assert calculator.mean_absolute_deviation() == round(
        sum(abs(float(x) - mean) for x in data.split(", ")) / len(data.split(", ")), 2
    )


# Test cases for standard_deviation function
def test_standard_deviation_valid_data():
    data = generate_random_data(1000)
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


def test_standard_deviation_negative_values():
    data = generate_random_data(1000)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    variance = sum((float(x) - mean) ** 2 for x in data.split(", ")) / len(
        data.split(", ")
    )
    assert calculator.standard_deviation() == round(variance**0.5, 2)


def test_standard_deviation_decimal_values():
    data = generate_random_data(1000, 0, 100)
    calculator = Calculator()
    calculator.input_data(data)
    mean = sum(map(float, data.split(", "))) / len(data.split(", "))
    variance = sum((float(x) - mean) ** 2 for x in data.split(", ")) / len(
        data.split(", ")
    )
    assert calculator.standard_deviation() == round(variance**0.5, 2)
