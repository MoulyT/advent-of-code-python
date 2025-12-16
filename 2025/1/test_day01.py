import pytest

from .day01 import (
    apply_rotation,
    count_times_ends_at_zero,
    count_times_pass_by_zero,
    extract_rotations,
)

EXAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_extract_rotations():
    result = extract_rotations(EXAMPLE_INPUT)
    assert result == (
        -68,
        -30,
        48,
        -5,
        60,
        -55,
        -1,
        -99,
        14,
        -82,
    )


@pytest.mark.parametrize(
    "initial_pos,rotation,expected_pos,expected_zeros",
    [
        (50, -68, 82, 1),
        (82, -30, 52, 0),
        (52, 48, 0, 1),
        (0, -5, 95, 0),
        (95, 60, 55, 1),
        (55, -55, 0, 1),
        (0, -1, 99, 0),
        (99, -99, 0, 1),
        (0, 14, 14, 0),
        (14, -82, 32, 1),
    ],
)
def test_apply_rotation(initial_pos, rotation, expected_pos, expected_zeros):
    final_position, zeros_crossed = apply_rotation(initial_pos, rotation)
    assert final_position == expected_pos
    assert zeros_crossed == expected_zeros


def test_count_times_ends_at_zero():
    assert (
        count_times_ends_at_zero(
            (
                -68,
                -30,
                48,
                -5,
                60,
                -55,
                -1,
                -99,
                14,
                -82,
            )
        )
        == 3
    )


def test_count_times_pass_by_zero():
    assert (
        count_times_pass_by_zero(
            (
                -68,
                -30,
                48,
                -5,
                60,
                -55,
                -1,
                -99,
                14,
                -82,
            )
        )
        == 6
    )


@pytest.mark.parametrize(
    "rotations,expected_passes",
    [
        # Should pass by zero exactly 1 time
        ((-75, 20), 1),  # L75, R20
        ((75, -20), 1),  # R75, L20
        ((-50, 50), 1),  # L50, R50
        ((-50, -50), 1),  # L50, L50
        ((50, 50), 1),  # R50, R50
        ((50, -50), 1),  # R50, L50
        ((120,), 1),
        ((-20,), 0),
        ((-90,), 1),
        ((-120,), 1),
        ((-150,), 2),
        # Should pass by zero exactly 2 times
        ((-200,), 2),  # L200
        ((200,), 2),  # R200
        ((-150, -50), 2),  # L150, L50
        ((-150, 50), 2),  # L150, R50
        ((150, -50), 2),  # R150, L50
        ((150, 50), 2),  # R150, R50
    ],
)
def test_count_times_pass_by_zero_comprehensive(rotations, expected_passes):
    assert count_times_pass_by_zero(rotations) == expected_passes


def test_part_one_solution():
    from pathlib import Path

    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, encoding="utf-8") as input_file:
        input_data = input_file.read()

    rotations = extract_rotations(input_data)
    result = count_times_ends_at_zero(rotations)
    assert result == 1195


def test_part_two_solution():
    from pathlib import Path

    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, encoding="utf-8") as input_file:
        input_data = input_file.read()

    rotations = extract_rotations(input_data)
    result = count_times_pass_by_zero(rotations)
    assert result == 6770
