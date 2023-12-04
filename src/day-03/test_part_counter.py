import pytest
from part_counter import Engine, EnginePointer
import part_counter


@pytest.mark.parametrize(
    "engine_string,expected",
    [
        (
            "",
            Engine([], []),
        ),
        (
            "1.23.4.*",
            Engine(
                [
                    EnginePointer(0, 0, 1),
                    EnginePointer(0, 2, 23),
                    EnginePointer(0, 5, 4),
                ],
                [EnginePointer(0, 7, "*")],
            ),
        ),
        (
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
            Engine(
                [
                    EnginePointer(0, 0, 467),
                    EnginePointer(0, 5, 114),
                    EnginePointer(2, 2, 35),
                    EnginePointer(2, 6, 633),
                    EnginePointer(4, 0, 617),
                    EnginePointer(5, 7, 58),
                    EnginePointer(6, 2, 592),
                    EnginePointer(7, 6, 755),
                    EnginePointer(9, 1, 664),
                    EnginePointer(9, 5, 598),
                ],
                [
                    EnginePointer(1, 3, "*"),
                    EnginePointer(3, 6, "#"),
                    EnginePointer(4, 3, "*"),
                    EnginePointer(5, 5, "+"),
                    EnginePointer(8, 3, "$"),
                    EnginePointer(8, 5, "*"),
                ],
            ),
        ),
    ],
)
def test_engine_deserialization(engine_string: str, expected: Engine):
    assert part_counter.deserialize_engine(engine_string) == expected


@pytest.mark.parametrize(
    "engine_string,expected",
    [
        (
            "",
            [],
        ),
        ("1.23.4.*", []),
        (
            "1.23.4*",
            [
                EnginePointer(0, 5, 4),
            ],
        ),
        (
            """1.23.4.*
...^...5""",
            [
                EnginePointer(0, 2, 23),
                EnginePointer(1, 7, 5),
            ],
        ),
        (
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
            [
                EnginePointer(0, 0, 467),
                EnginePointer(2, 2, 35),
                EnginePointer(2, 6, 633),
                EnginePointer(4, 0, 617),
                EnginePointer(6, 2, 592),
                EnginePointer(7, 6, 755),
                EnginePointer(9, 1, 664),
                EnginePointer(9, 5, 598),
            ],
        ),
    ],
)
def test_engine_list_valid_part_nums(engine_string: str, expected: list[EnginePointer]):
    assert (
        part_counter.deserialize_engine(engine_string)._filter_valid_part_nums()
        == expected
    )


@pytest.mark.parametrize(
    "engine_string,expected",
    [
        (
            "",
            0,
        ),
        ("1.23.4.*", 0),
        (
            "1.23.4*",
            4,
        ),
        (
            """1.23.4.*
...^...5""",
            28,
        ),
        (
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
            4361,
        ),
    ],
)
def test_engine_list_valid_part_num_sum(engine_string: str, expected: int):
    assert (
        part_counter.deserialize_engine(engine_string).get_valid_part_nums_sum()
        == expected
    )


@pytest.mark.parametrize(
    "path_str,expected",
    [
        (
            "src/day-03/resources/test_input",
            4361,
        ),
        (
            "src/day-03/resources/input",
            532331,
        ),
    ],
)
def test_engine_list_valid_part_num_sum_from_file(path_str: str, expected: int):
    assert part_counter.count_valid_part_nums_sum_from_path(path_str) == expected


@pytest.mark.parametrize(
    "engine_string,expected",
    [
        (
            "",
            0,
        ),
        ("1.23.4.*", 0),
        ("1.23.4*", 0),
        (
            """1.23.4*
...^..5""",
            20,
        ),
        (
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
            467835,
        ),
    ],
)
def test_count_gear_ratio_sum(engine_string: str, expected: int):
    assert part_counter.count_gear_ratio_sum(engine_string) == expected


@pytest.mark.parametrize(
    "path_str,expected",
    [
        (
            "src/day-03/resources/test_input",
            467835,
        ),
        (
            "src/day-03/resources/input",
            82301120,
        ),
    ],
)
def test_count_gear_ratio_sum_from_path(path_str: str, expected: int):
    assert part_counter.count_gear_ratio_sum_from_path(path_str) == expected
