import pytest
import calibrator


@pytest.mark.parametrize(
    "test_string,test_n,expected",
    [
        ("1abc2", 2, ["1a", "ab", "bc", "c2", "2"]),
        ("1abc2", 3, ["1ab", "abc", "bc2", "c2", "2"]),
    ],
)
def test_create_line_ngrams(test_string: str, test_n: int, expected: int):
    assert calibrator.create_line_ngrams(test_string, test_n) == expected


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
    assert (
        calibrator.get_first_digit_in_ngrams(calibrator.create_line_ngrams(test_input))
        == expected
    )


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
    assert (
        calibrator.get_first_digit_in_ngrams(
            calibrator.create_line_ngrams(test_input)[::-1]
        )
        == expected
    )


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


@pytest.mark.parametrize(
    "test_path,replace_words,expected",
    [
        ("src/day-01/resources/test_input_part_1", False, 142),
        ("src/day-01/resources/test_input_part_2", True, 281),
    ],
)
def test_get_file_calibration_from_website_data(
    test_path: str, replace_words: bool, expected: int
):
    assert calibrator.get_file_calibration(test_path, replace_words) == expected
