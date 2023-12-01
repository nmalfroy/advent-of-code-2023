# Find the first digit in a string.  If no digit is found, return 0.
def get_first_digit(line: str) -> int:
    for char in line:
        if char.isdecimal():
            return int(char)
    return 0


# Find the last digit in a string.  If no digit is found, return 0.
def get_last_digit(line: str) -> int:
    return get_first_digit(line[::-1])


# Calibrate a line by finding the first and last digits and combining them into a two digit number.
def get_line_calibration(line: str) -> int:
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    return int(f"{first_digit}{last_digit}")


def get_file_calibration(file_path: str) -> int:
    with open(file_path, "r") as f:
        calibration = 0
        for line in f:
            calibration += get_line_calibration(line)
        return calibration


if __name__ == "__main__":
    print(get_file_calibration("src/day-1/resources/input"))
