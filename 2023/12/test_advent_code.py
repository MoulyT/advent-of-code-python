from advent_code import (
    EXAMPLE_INPUT,
    parse_input,
    unfold_springs,
    is_possible_springs,
    how_many_possible_springs,
)


def test_parse_input():
    assert parse_input(EXAMPLE_INPUT) == [
        ("???.###", (1, 1, 3)),
        (".??..??...?##.", (1, 1, 3)),
        ("?#?#?#?#?#?#?#?", (1, 3, 1, 6)),
        ("????.#...#...", (4, 1, 1)),
        ("????.######..#####.", (1, 6, 5)),
        ("?###????????", (3, 2, 1)),
    ]


def test_unfold_springs():
    input_data = [("???.###", (1, 1, 3)), (".#", (1,))]
    expected_output = [
        (
            "???.###????.###????.###????.###????.###",
            (1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3),
        ),
        (".#?.#?.#?.#?.#", (1, 1, 1, 1, 1)),
    ]

    assert unfold_springs(input_data) == expected_output


# Possible springs
#     #.#.### 1,1,3
#     .#...#....###. 1,1,3
#     .#.###.#.###### 1,3,1,6
#     ####.#...#... 4,1,1
#     #....######..#####. 1,6,5
#     .###.##....# 3,2,1


def test_is_possible_springs():
    assert is_possible_springs("#.#.###", (1, 1, 3)) is True
    assert is_possible_springs(".#...#....###.", (1, 1, 3)) is True
    assert is_possible_springs(".#.###.#.######", (1, 3, 1, 6)) is True
    assert is_possible_springs("####.#...#...", (4, 1, 1)) is True
    assert is_possible_springs("#....######..#####.", (1, 6, 5)) is True
    assert is_possible_springs(".###.##....#", (3, 2, 1)) is True

    assert is_possible_springs("##.###", (1, 1, 3)) is False
    assert is_possible_springs(".##...#....###.", (1, 1, 3)) is False
    assert is_possible_springs(".#.###.#.#######", (1, 3, 1, 6)) is False
    assert is_possible_springs(".###.##.#.##", (3, 2, 1)) is False


# How many possible arrangements?
# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangements


def test_how_many_possible_springs():
    assert how_many_possible_springs("#.#.###", (1, 1, 3)) == 1
    assert how_many_possible_springs(".??..??...?##.", (1, 1, 3)) == 4
    assert how_many_possible_springs("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert how_many_possible_springs("????.#...#...", (4, 1, 1)) == 1
    assert how_many_possible_springs("????.######..#####.", (1, 6, 5)) == 4
    assert how_many_possible_springs("?###????????", (3, 2, 1)) == 10
