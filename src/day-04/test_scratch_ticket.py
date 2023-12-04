import pytest
from scratch_ticket import ScratchTicket
import scratch_ticket


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Ticket 1: 1 2 3 | 2 3 4", ScratchTicket(1, [1, 2, 3], [2, 3, 4])),
        ("Ticket 2: 1 2 3 | 4 5 6", ScratchTicket(2, [1, 2, 3], [4, 5, 6])),
    ],
)
def test_from_string(str: str, expected: ScratchTicket):
    assert ScratchTicket.from_string(str) == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Ticket 1: 1 2 3 | 2 3 4", [2, 3]),
        ("Ticket 2: 1 2 3 | 4 5 6", []),
    ],
)
def test_get_matched_numbers(str: str, expected: ScratchTicket):
    assert ScratchTicket.from_string(str).get_matched_numbers() == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Ticket 1: 1 2 3 | 2 3 4", 2),
        ("Ticket 2: 1 2 3 | 4 5 6", 0),
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14 1", 2),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
    ],
)
def test_get_matched_value(str: str, expected: int):
    assert ScratchTicket.from_string(str).get_matched_value() == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("src/day-04/resources/test_input", 13),
        ("src/day-04/resources/input", 25010),
    ],
)
def test_count_scratch_from_file(path: str, expected: int):
    assert scratch_ticket.count_scratch_from_file(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("src/day-04/resources/test_input", 30),
        ("src/day-04/resources/input", 9924412),
    ],
)
def test_count_scratch_tickets_from_file(path: str, expected: int):
    assert scratch_ticket.count_scratch_tickets_from_file(path) == expected
