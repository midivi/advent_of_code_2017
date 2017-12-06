from collections import defaultdict
import pytest


def solve(input):
    all_seen_dict = defaultdict(int)
    next_arrangement = tuple(input)
    while True:
        next_arrangement = get_gext_arrangement(next_arrangement)
        if next_arrangement in all_seen_dict:
            return len(all_seen_dict) + 1
        all_seen_dict[next_arrangement]


def get_gext_arrangement(input: tuple) -> tuple:
    output = list(input)
    maximum_value = max(output)
    maximum_index = output.index(maximum_value)
    length_input = len(input)
    output[maximum_index] = 0
    for counter in range(maximum_index + 1, maximum_index + maximum_value + 1):
        index = counter % length_input
        output[index] += 1
    return tuple(output)


if __name__ == "__main__":
    input = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
    print(solve(input))


@pytest.mark.parametrize('input, expected', [
    ((0, 2, 7, 0), (2, 4, 1, 2))
])
def test_get_next_arrangement(input, expected):
    assert get_gext_arrangement(input) == expected


def test_solve():
    assert solve((0, 2, 7, 0)) == 5