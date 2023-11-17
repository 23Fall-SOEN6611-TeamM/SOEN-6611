import pytest
from statistic_tool.calculator import Calculator


# Test cases for minimum function
def test_minimum_valid_data():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2")
    assert calculator.minimum() == 1.0


def test_minimum_no_data():
    calculator = Calculator()
    assert calculator.minimum() is None


def test_minimum_negative_values():
    calculator = Calculator()
    calculator.input_data("-3, -1, -4, -1, -5, -9, -2")
    assert calculator.minimum() == -9.0


def test_minimum_duplicate_values():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2, 1")
    assert calculator.minimum() == 1.0


# Test cases for maximum function
def test_maximum_valid_data():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2")
    assert calculator.maximum() == 9.0


def test_maximum_no_data():
    calculator = Calculator()
    assert calculator.maximum() is None


def test_maximum_negative_values():
    calculator = Calculator()
    calculator.input_data("-3, -1, -4, -1, -5, -9, -2")
    assert calculator.maximum() == -1.0


def test_maximum_duplicate_values():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2, 5")
    assert calculator.maximum() == 9.0


# Test cases for mode function
def test_mode_valid_data_single_mode():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2, 5, 6, 5")
    assert calculator.mode() == [5.0]


def test_mode_valid_data_multiple_modes():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2, 5, 6, 5, 6")
    assert calculator.mode() == [5.0]


def test_mode_no_data():
    calculator = Calculator()
    assert calculator.mode() is None


def test_mode_all_unique_values():
    calculator = Calculator()
    calculator.input_data("1, 2, 3, 4, 5")
    assert calculator.mode() == [1, 2, 3, 4, 5]


# Test cases for median function
def test_median_valid_data_odd():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2")
    assert calculator.median() == 3.0


def test_median_valid_data_even():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2, 6")
    assert calculator.median() == 3.5


def test_median_no_data():
    calculator = Calculator()
    assert calculator.median() is None


def test_median_duplicate_values():
    calculator = Calculator()
    calculator.input_data("3, 1, 4, 1, 5, 9, 2, 6, 2, 6")
    assert calculator.median() == 3.5


# Test cases for mean function
def test_mean_valid_data():
    calculator = Calculator()
    calculator.input_data("1, 2, 3, 4, 5")
    assert calculator.mean() == 3.0


def test_mean_no_data():
    calculator = Calculator()
    assert calculator.mean() is None


def test_mean_negative_values():
    calculator = Calculator()
    calculator.input_data("-1, -2, -3, -4, -5")
    assert calculator.mean() == -3.0


def test_mean_decimal_values():
    calculator = Calculator()
    calculator.input_data("1.5, 2.5, 3.5, 4.5, 5.5")
    assert calculator.mean() == 3.5


# Test cases for mean_absolute_deviation function
def test_mean_absolute_deviation_valid_data():
    calculator = Calculator()
    calculator.input_data("1, 2, 3, 4, 5")
    assert calculator.mean_absolute_deviation() == 1.2


def test_mean_absolute_deviation_no_data():
    calculator = Calculator()
    assert calculator.mean_absolute_deviation() is None


def test_mean_absolute_deviation_negative_values():
    calculator = Calculator()
    calculator.input_data("-1, -2, -3, -4, -5")
    assert calculator.mean_absolute_deviation() == 1.2


def test_mean_absolute_deviation_decimal_values():
    calculator = Calculator()
    calculator.input_data("1.5, 2.5, 3.5, 4.5, 5.5")
    assert calculator.mean_absolute_deviation() == 1.2


# Test cases for standard_deviation function
def test_standard_deviation_valid_data():
    calculator = Calculator()
    calculator.input_data("1, 2, 3, 4, 5")
    assert calculator.standard_deviation() == 1.41  # Rounded to two decimal places


def test_standard_deviation_no_data():
    calculator = Calculator()
    assert calculator.standard_deviation() is None


def test_standard_deviation_negative_values():
    calculator = Calculator()
    calculator.input_data("-1, -2, -3, -4, -5")
    assert calculator.standard_deviation() == 1.41  # Rounded to two decimal places


def test_standard_deviation_decimal_values():
    calculator = Calculator()
    calculator.input_data("1.5, 2.5, 3.5, 4.5, 5.5")
    assert calculator.standard_deviation() == 1.41  # Rounded to two decimal places
