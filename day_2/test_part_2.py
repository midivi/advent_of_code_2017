from itertools import combinations


def solve(file_input):
    checksum_total = 0
    for line in file_input:
        line_array = map(lambda x: int(x), line.split())
        line_combinations = combinations(line_array, 2)
        match = [(x, y) for (x, y) in line_combinations if not x % y or not y % x]
        assert len(match) == 1
        den, num = sorted(match[0])
        checksum_total = checksum_total + num / den

    return checksum_total


if __name__ == "__main__":
    fh = open('input.txt')
    print(solve(fh))
