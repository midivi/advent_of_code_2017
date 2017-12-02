import pytest


def solve(numbers: str, total: int):
    total = 0
    for i in range(0, len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            total = total + int(numbers[i])
    if numbers[0] == numbers[-1]:
        total = total + int(numbers[-1])
    return total


@pytest.mark.parametrize("input, answer", [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9),
])
def test_sanity(input, answer):
    assert solve(input, 0) == answer


file = open('input.txt')
input = file.readlines()[0].strip()

print(solve(input, 0))
