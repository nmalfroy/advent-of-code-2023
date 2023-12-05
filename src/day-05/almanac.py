from typing import NamedTuple
from typing_extensions import Self
from enum import StrEnum


class Category(StrEnum):
    SEED = "seed"
    SOIL = "soil"
    FERTILIZER = "fertilizer"
    WATER = "water"
    LIGHT = "light"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    lOCATION = "location"


class MappedInt(NamedTuple):
    num: int
    mapped: bool


class SeedMapper(NamedTuple):
    dest_range: int
    src_range_start: int
    src_range_length: int

    def map_seed(self, src_seed: int) -> MappedInt:
        src_range_end = self.src_range_start + self.src_range_length
        if src_seed < self.src_range_start or src_seed >= src_range_end:
            return MappedInt(src_seed, False)
        return MappedInt(self.dest_range + (src_seed - self.src_range_start), True)

    @staticmethod
    def from_string(string: str) -> Self:
        dest_range, src_range_start, src_range_length = string.split(" ")
        return SeedMapper(int(dest_range), int(src_range_start), int(src_range_length))


class SeedMapperCategory(NamedTuple):
    src_category: Category
    dest_category: Category
    mappers: list[SeedMapper]

    def map_seed(self, src_seed: int) -> int:
        for mapper in self.mappers:
            mapped_seed = mapper.map_seed(src_seed)
            if mapped_seed.mapped:
                return mapped_seed.num

        return src_seed

    @staticmethod
    def from_string(string: str) -> Self:
        title, mappers = string.split(" map:\n")
        src_category, dest_category = title.split("-to-")
        mappers = [
            SeedMapper.from_string(mapper) for mapper in mappers.strip().split("\n")
        ]
        return SeedMapperCategory(
            Category(src_category), Category(dest_category), mappers
        )


class Almanac(NamedTuple):
    seeds: list[int]
    categories: list[SeedMapperCategory]

    @staticmethod
    def from_string(string: str) -> Self:
        sections = string.strip().split("\n\n")
        seeds_str = sections[0].replace("seeds: ", "")
        seeds = [int(seed) for seed in seeds_str.strip().split(" ")]
        categories = [
            SeedMapperCategory.from_string(category.strip())
            for category in sections[1:]
        ]
        return Almanac(seeds, categories)

    def _find_category_by_source(self, src_category: Category) -> SeedMapperCategory:
        for category in self.categories:
            if category.src_category == src_category:
                return category

        return None

    def map_seed(self, src_seed: int) -> int:
        seed = src_seed
        category = self._find_category_by_source(Category.SEED)
        while category != None:
            seed = category.map_seed(seed)
            category = self._find_category_by_source(category.dest_category)
        return seed


def load_and_return_seed_locations(path: str) -> list[int]:
    with open(path) as f:
        almanac = Almanac.from_string(f.read())
        return [almanac.map_seed(seed) for seed in almanac.seeds]


def load_and_return_min_seed_location(path: str) -> int:
    return min(load_and_return_seed_locations(path))
