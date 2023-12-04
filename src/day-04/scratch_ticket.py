from typing import NamedTuple
from typing_extensions import Self
from math import floor
import re


class ScratchTicket(NamedTuple):
    ticket_number: int
    winning_numbers: list[int]
    match_numbers: list[int]

    # Return the winning numbers that have match_numbers
    def get_matched_numbers(self) -> list[int]:
        return list(set(self.winning_numbers).intersection(self.match_numbers))

    # Return the value of the scratch ticket based of numbers that have match_numbers (each match multiplies value by 2 with single match being 1)
    def get_matched_value(self) -> int:
        return floor(2 ** (len(self.get_matched_numbers()) - 1))

    @staticmethod
    def from_string(string: str) -> Self:
        ticket_number_str, numbers = string.split(":")
        ticket_number = int(re.split("\\s+", ticket_number_str)[1].strip())
        winning_numbers, match_numbers = numbers.split("|")
        return ScratchTicket(
            ticket_number,
            [int(num) for num in re.split("\\s+", winning_numbers.strip())],
            [int(num) for num in re.split("\\s+", match_numbers.strip())],
        )


def count_tickets(
    scratch_tickets: list[ScratchTicket],
    start_index: int,
    end_index: int,
    start_count: int,
) -> int:
    for i, ticket in enumerate(scratch_tickets[start_index:end_index]):
        num_matches = len(ticket.get_matched_numbers())
        start_count += count_tickets(
            scratch_tickets,
            start_index + 1 + i,
            start_index + 1 + i + num_matches,
            1,
        )
    return start_count


def count_scratch_from_file(path: str) -> int:
    with open(path) as f:
        scratch_tickets = [ScratchTicket.from_string(line) for line in f.readlines()]
        return sum([ticket.get_matched_value() for ticket in scratch_tickets])


def count_scratch_tickets_from_file(path: str) -> int:
    with open(path) as f:
        scratch_tickets = [ScratchTicket.from_string(line) for line in f.readlines()]
        return count_tickets(scratch_tickets, 0, len(scratch_tickets), 0)
