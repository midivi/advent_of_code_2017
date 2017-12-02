import pytest


def solve(numbers: str, total: int):
    total = 0
    half_numbers_length = int((len(numbers)) / 2)
    for i in range(0, half_numbers_length):
        if numbers[i] == numbers[i + half_numbers_length]:
            total = total + int(numbers[i])
    return total * 2


@pytest.mark.parametrize("input, answer", [
    ("1212", 6),
    ("1221", 0),
    ("123425", 4),
    ("123123", 12),
    ("12131415", 4),
])
def test_sanity(input, answer):
    assert solve(input, 0) == answer


file = open('input.txt')
input = file.readlines()[0].strip()

print(solve(input, 0))
