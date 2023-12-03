import pytest

import game
from game import ColorCollection, Game


@pytest.mark.parametrize(
    "test_string,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Game(
                1,
                [
                    ColorCollection(num_red=4, num_green=0, num_blue=3),
                    ColorCollection(num_red=1, num_green=2, num_blue=6),
                    ColorCollection(num_red=0, num_green=2, num_blue=0),
                ],
            ),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            Game(
                2,
                [
                    ColorCollection(num_red=0, num_green=2, num_blue=1),
                    ColorCollection(num_red=1, num_green=3, num_blue=4),
                    ColorCollection(num_red=0, num_green=1, num_blue=1),
                ],
            ),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            Game(
                3,
                [
                    ColorCollection(num_red=20, num_green=8, num_blue=6),
                    ColorCollection(num_red=4, num_green=13, num_blue=5),
                    ColorCollection(num_red=1, num_green=5, num_blue=0),
                ],
            ),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            Game(
                4,
                [
                    ColorCollection(num_red=3, num_green=1, num_blue=6),
                    ColorCollection(num_red=6, num_green=3, num_blue=0),
                    ColorCollection(num_red=14, num_green=3, num_blue=15),
                ],
            ),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            Game(
                5,
                [
                    ColorCollection(num_red=6, num_green=3, num_blue=1),
                    ColorCollection(num_red=1, num_green=2, num_blue=2),
                ],
            ),
        ),
    ],
)
def test_deserialize_game(test_string: str, expected: game.Game):
    assert game.deserialize_game(test_string) == expected


@pytest.mark.parametrize(
    "test_game,bag_content,expected_value",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            True,
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            True,
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            False,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            False,
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            True,
        ),
    ],
)
def test_is_bag_content_possible(
    test_game: str, bag_content: ColorCollection, expected_value: bool
):
    assert (
        game.is_bag_content_possible(
            bag_content,
            game.deserialize_game(test_game).peeks,
        )
        == expected_value
    )


@pytest.mark.parametrize(
    "test_path,bag_content,expected_count",
    [
        (
            "src/day-02/resources/test_input_part_1",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            8,
        ),
        (
            "src/day-02/resources/input",
            ColorCollection(num_red=12, num_green=13, num_blue=14),
            2061,
        ),
    ],
)
def test_run_game_check(
    test_path: str, bag_content: ColorCollection, expected_count: int
):
    assert game.run_game_check(test_path, bag_content) == expected_count


@pytest.mark.parametrize(
    "test_game,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            ColorCollection(num_red=4, num_green=2, num_blue=6),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            ColorCollection(num_red=1, num_green=3, num_blue=4),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            ColorCollection(num_red=20, num_green=13, num_blue=6),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            ColorCollection(num_red=14, num_green=3, num_blue=15),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ColorCollection(num_red=6, num_green=3, num_blue=2),
        ),
    ],
)
def test_min_bag_sizes(test_game: str, expected: ColorCollection):
    assert (
        game.get_minimum_bag_size(
            game.deserialize_game(test_game).peeks,
        )
        == expected
    )


@pytest.mark.parametrize(
    "test_game,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            48,
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            12,
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            1560,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            630,
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            36,
        ),
    ],
)
def test_bag_power(test_game: str, expected: int):
    assert (
        game.get_minimum_bag_size(
            game.deserialize_game(test_game).peeks,
        ).get_power()
        == expected
    )


@pytest.mark.parametrize(
    "test_path,expected_count",
    [
        (
            "src/day-02/resources/test_input_part_1",
            2286,
        ),
        (
            "src/day-02/resources/input",
            72596,
        ),
    ],
)
def test_get_game_power_sum(test_path: str, expected_count: int):
    assert game.get_game_power_sum(test_path) == expected_count
