NUMBER_REPLACEMENTS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
MAX_NGRAM_SIZE = len(max(NUMBER_REPLACEMENTS.keys(), key=len))


# Create ngrams from a string. For example, create_line_ngrams("abc", 2) returns ["ab", "bc"].
# n is a parameter for testing but the default is the max ngram size for this problem which is the maximim
# number name length.
def create_line_ngrams(line: str, n: int = MAX_NGRAM_SIZE) -> list[str]:
    ngrams = []
    for i in range(len(line)):
        ngrams.append(line[i : i + n])
    return ngrams


# Find the first digit in a string.  If no digit is found, return -1
def get_first_digit_in_string(string: str, replace_number_words: bool = False) -> int:
    if string[0].isdecimal():
        return int(string[0])
    if replace_number_words:
        # Can further optimize by short-circuiting if the first letter isn't one of the number name first letters
        for key, value in NUMBER_REPLACEMENTS.items():
            if string.startswith(key):
                return int(value)
    return -1


# Find the first digit in an ordered list of ngrams. If no digit is found, return 0.
def get_first_digit_in_ngrams(
    line_n_grams: list[str], replace_number_words: bool = False
) -> int:
    for ngram in line_n_grams:
        digit = get_first_digit_in_string(ngram, replace_number_words)
        if digit != -1:
            return digit
    return 0


# Calibrate a line by finding the first and last digits and combining them into a two digit number.
def get_line_calibration(line: str, replace_number_words: bool = False) -> int:
    n_grams = create_line_ngrams(line)
    first_digit = get_first_digit_in_ngrams(n_grams, replace_number_words)
    # reverse the n-grams to find the last digit
    last_digit = get_first_digit_in_ngrams(n_grams[::-1], replace_number_words)
    return int(f"{first_digit}{last_digit}")


# Calibrate a file by calibrating each line and summing the results.
# Optionally, replace number words with actual numbers in the file before calibrating.
def get_file_calibration(file_path: str, replace_number_words: bool = True) -> int:
    with open(file_path, "r") as f:
        calibration = 0
        for line in f:
            calibration += get_line_calibration(line, replace_number_words)
        return calibration


if __name__ == "__main__":
    print(get_file_calibration("src/day-1/resources/input"))
