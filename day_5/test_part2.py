from typing import List


def solve(input: List) -> int:
    current_index = 0
    steps = 0
    while 0 <= current_index < len(input):
        jump = input[current_index]
        offset = -1 if jump >= 3 else 1
        input[current_index] += offset
        current_index += jump
        steps += 1
    return steps


if __name__ == "__main__":
    file = open('input.txt')
    input = list(map(lambda x: int(x.strip()), list(file)))
    print(solve(input))


def test_solve():
    input = [0, 3, 0, 1, -3]

    assert solve(input) == 10
