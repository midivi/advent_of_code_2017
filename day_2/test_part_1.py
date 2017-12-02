def solve(file_input):
    checksum_total = 0
    for line in file_input:
        line_array = list(map(lambda x: int(x), line.split()))
        line_checksum = max(line_array) - min(line_array)
        checksum_total = line_checksum + checksum_total
    return checksum_total


if __name__ == "__main__":
    fh = open('input.txt')
    print(solve(fh))
