from typing import NamedTuple
from typing_extensions import Self


# Pointer to a part number or symbol in an engine.
class EnginePointer(NamedTuple):
    line: int
    start: int
    value: str | int

    def overlaps_with(self, other: Self) -> bool:
        # Build the rectangle around self.
        collide_rect = Rect(
            start_pos=self.start,
            start_line=max(self.line - 1, 0),
            end_pos=self.start + len(str(self.value)),
            end_line=self.line + 1,
        )
        return (
            (
                other.start >= collide_rect.start_pos
                and other.start <= collide_rect.end_pos
            )
            or (
                other.start + len(str(other.value)) >= collide_rect.start_pos
                and other.start + len(str(other.value)) <= collide_rect.end_pos
            )
        ) and (
            other.line >= collide_rect.start_line
            and other.line <= collide_rect.end_line
        )


class Rect(NamedTuple):
    start_pos: int
    start_line: int
    end_pos: int
    end_line: int


# Contains all information about an engine.
class Engine(NamedTuple):
    part_nums: list[EnginePointer]
    symbols: list[EnginePointer]

    def _filter_valid_part_nums(self) -> list[EnginePointer]:
        part_nums = []
        for part_num in self.part_nums:
            # is there an adjoining symbol?
            for symbol in self.symbols:
                if part_num.overlaps_with(symbol):
                    part_nums.append(part_num)
                    break
        return part_nums

    def get_valid_part_nums_sum(self) -> list[EnginePointer]:
        part_num_sum = 0
        for part_num in self._filter_valid_part_nums():
            part_num_sum += part_num.value
        return part_num_sum

    def get_attached_part_nums(self, symbol: EnginePointer) -> list[EnginePointer]:
        part_nums = []
        for part_num in self.part_nums:
            if part_num.overlaps_with(symbol):
                part_nums.append(part_num)
        return part_nums

    def get_gear_ratio_sum(self) -> int:
        gears_ratio_sums = 0
        for symbol in self.symbols:
            # are there at least two adjoining part_nums?
            if symbol.value == "*":
                attached_part_nums = self.get_attached_part_nums(symbol)
                if len(attached_part_nums) >= 2:
                    gear_ratio = 1
                    for part_num in attached_part_nums:
                        gear_ratio *= part_num.value
                    gears_ratio_sums += gear_ratio
        return gears_ratio_sums


def char_is_part_num_part(char: str) -> bool:
    return char.isdecimal()


def char_is_symbol(char: str) -> bool:
    return not char.isdecimal() and char != "."


def deserialize_engine_line(line: str, line_num: int, engine: Engine) -> None:
    part_num_builder = ""
    symbol_builder = ""
    for i, char in enumerate(line):
        if char_is_part_num_part(char):
            part_num_builder += char
            if i + 1 == len(line) or not char_is_part_num_part(line[i + 1]):
                engine.part_nums.append(
                    EnginePointer(
                        line=line_num,
                        start=(i + 1) - len(part_num_builder),
                        value=int(part_num_builder),
                    )
                )
                part_num_builder = ""
        elif char_is_symbol(char):
            symbol_builder += char
            if i + 1 == len(line) or not char_is_symbol(line[i + 1]):
                engine.symbols.append(
                    EnginePointer(
                        line=line_num,
                        start=(i + 1) - len(symbol_builder),
                        value=symbol_builder,
                    )
                )
                symbol_builder = ""


def deserialize_engine(engine_string: str) -> Engine:
    engine = Engine([], [])
    for line_num, line in enumerate(engine_string.splitlines()):
        deserialize_engine_line(line, line_num, engine)
    return engine


def count_valid_part_nums_sum(engine_string: str) -> int:
    engine = deserialize_engine(engine_string)
    return engine.get_valid_part_nums_sum()


def count_valid_part_nums_sum_from_path(path: str) -> int:
    with open(path, "r") as f:
        engine_string = f.read()
        return count_valid_part_nums_sum(engine_string)


def count_gear_ratio_sum(engine_string: str) -> int:
    engine = deserialize_engine(engine_string)
    return engine.get_gear_ratio_sum()


def count_gear_ratio_sum_from_path(path: str) -> int:
    with open(path, "r") as f:
        engine_string = f.read()
        return count_gear_ratio_sum(engine_string)
