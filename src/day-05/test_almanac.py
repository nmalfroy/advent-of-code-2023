import pytest
from almanac import MappedInt, SeedMapper, SeedMapperCategory, Category, Almanac
import almanac


@pytest.mark.parametrize(
    "mapper,seed,expected",
    [
        (SeedMapper(50, 98, 2), 10, MappedInt(10, False)),
        (SeedMapper(50, 98, 2), 98, MappedInt(50, True)),
        (SeedMapper(50, 98, 2), 99, MappedInt(51, True)),
        (SeedMapper(50, 98, 2), 100, MappedInt(100, False)),
    ],
)
def test_range_map(mapper: SeedMapper, seed: int, expected: int):
    assert mapper.map_seed(seed) == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        ("50 98 2", SeedMapper(50, 98, 2)),
        ("52 50 48", SeedMapper(52, 50, 48)),
    ],
)
def test_serialize_seed_map(str: str, expected: SeedMapper):
    assert SeedMapper.from_string(str) == expected


@pytest.mark.parametrize(
    "mapper_category,seed,expected",
    [
        (
            SeedMapperCategory(
                Category.SEED,
                Category.SOIL,
                [SeedMapper(50, 98, 2), SeedMapper(52, 50, 48)],
            ),
            79,
            81,
        ),
    ],
)
def test_category_range_map(
    mapper_category: SeedMapperCategory, seed: int, expected: int
):
    assert mapper_category.map_seed(seed) == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        (
            """seed-to-soil map:
50 98 2
52 50 48
""",
            SeedMapperCategory(
                Category.SEED,
                Category.SOIL,
                [SeedMapper(50, 98, 2), SeedMapper(52, 50, 48)],
            ),
        ),
    ],
)
def test_serialize_seed_map_categories(str: str, expected: SeedMapper):
    assert SeedMapperCategory.from_string(str) == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        (
            """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15
""",
            Almanac(
                [79, 14, 55, 13],
                [
                    SeedMapperCategory(
                        Category.SEED,
                        Category.SOIL,
                        [SeedMapper(50, 98, 2), SeedMapper(52, 50, 48)],
                    ),
                    SeedMapperCategory(
                        Category.SOIL,
                        Category.FERTILIZER,
                        [
                            SeedMapper(0, 15, 37),
                            SeedMapper(37, 52, 2),
                            SeedMapper(39, 0, 15),
                        ],
                    ),
                ],
            ),
        ),
    ],
)
def test_serialize_almanac(str: str, expected: Almanac):
    assert Almanac.from_string(str) == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        ("src/day-05/resources/test_input", [82, 43, 86, 35]),
    ],
)
def test_serialize_almanac(str: str, expected: Almanac):
    assert almanac.load_and_return_seed_locations(str) == expected


@pytest.mark.parametrize(
    "str,expected",
    [
        ("src/day-05/resources/test_input", 35),
        ("src/day-05/resources/input", 424490994),
    ],
)
def test_serialize_almanac(str: str, expected: Almanac):
    assert almanac.load_and_return_min_seed_location(str) == expected
