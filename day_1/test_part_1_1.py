import pytest


def solve(numbers: str, total: int):
    if len(numbers) == 1:
        return total
    if numbers[0] == numbers[1]:
        return solve(numbers[1::], total + int(numbers[0]))
    else:
        return solve(numbers[1::], total)


@pytest.mark.parametrize("input, answer", [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 0)
])
def test_sanity(input, answer):
    assert solve(input, 0) == answer


file = open('input.txt')
input = file.readlines()[0]

print(solve(input, 0))
