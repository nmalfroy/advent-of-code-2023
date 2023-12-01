import pytest
import calibrator


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1abc2", 1),
        ("pqr3stu8vwx", 3),
        ("a1b2c3d4e5f", 1),
        ("treb7uchet", 7),
        ("nodigits", 0),
    ],
)
def test_get_first_digit(test_input: str, expected: int):
    assert calibrator.get_first_digit(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1abc2", 2),
        ("pqr3stu8vwx", 8),
        ("a1b2c3d4e5f", 5),
        ("treb7uchet", 7),
        ("nodigits", 0),
    ],
)
def test_get_last_digit(test_input: str, expected: int):
    assert calibrator.get_last_digit(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("nodigits", 0),
    ],
)
def test_get_line_calibration(test_input: str, expected: int):
    assert calibrator.get_line_calibration(test_input) == expected


def test_get_file_calibration_from_website_data():
    assert calibrator.get_file_calibration("src/day-1/resources/test_input") == 142
