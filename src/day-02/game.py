from typing import NamedTuple


class ColorCollection(NamedTuple):
    num_red: int = 0
    num_green: int = 0
    num_blue: int = 0

    def get_power(self) -> int:
        return self.num_red * self.num_green * self.num_blue


class Game(NamedTuple):
    game_number: int
    peeks: list[ColorCollection]


# If the bag content is possible, return True. Otherwise, return False.
# The method loops through bag peeks and checks if the bag content is possible given the peek.
def is_bag_content_possible(
    bag_content: ColorCollection, peeks: list[ColorCollection]
) -> None:
    for peek in peeks:
        if (
            bag_content.num_red < peek.num_red
            or bag_content.num_green < peek.num_green
            or bag_content.num_blue < peek.num_blue
        ):
            return False

    return True


# Get the smallest bag that could pass all peeks for a game.
def get_minimum_bag_size(peeks: list[ColorCollection]) -> ColorCollection:
    max_num_red = 0
    max_num_green = 0
    max_num_blue = 0
    for peek in peeks:
        if peek.num_red > max_num_red:
            max_num_red = peek.num_red
        if peek.num_green > max_num_green:
            max_num_green = peek.num_green
        if peek.num_blue > max_num_blue:
            max_num_blue = peek.num_blue

    return ColorCollection(
        num_red=max_num_red, num_green=max_num_green, num_blue=max_num_blue
    )


def deserialize_game(line: str) -> Game:
    line_splits = line.split(":")
    name = line_splits[0].strip()
    game_number = int(name.split(" ")[1])
    peeks = []
    for peek in line_splits[1].strip().split(";"):
        num_red = 0
        num_green = 0
        num_blue = 0
        for peek_color in peek.split(","):
            peek_splits = peek_color.strip().split(" ")
            color_name = peek_splits[1].strip()
            match color_name:
                case "red":
                    num_red = int(peek_splits[0].strip())
                case "green":
                    num_green = int(peek_splits[0].strip())
                case "blue":
                    num_blue = int(peek_splits[0].strip())
        peeks.append(
            ColorCollection(num_red=num_red, num_green=num_green, num_blue=num_blue)
        )
    return Game(game_number=game_number, peeks=peeks)


# Returns the sum of game numbers for games where the bag content is possible.
def run_game_check(file_path: str, bag_content: ColorCollection) -> int:
    game_count = 0
    with open(file_path, "r") as f:
        for line in f:
            game = deserialize_game(line)
            if is_bag_content_possible(bag_content, game.peeks):
                game_count += game.game_number

    return game_count


def get_game_power_sum(file_path: str) -> int:
    get_game_power_sum = 0
    with open(file_path, "r") as f:
        for line in f:
            game = deserialize_game(line)
            get_game_power_sum += get_minimum_bag_size(game.peeks).get_power()

    return get_game_power_sum
