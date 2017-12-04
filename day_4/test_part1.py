from collections import Counter


def solve(input_file):
    valid_count = 0
    for line in input_file:
        passwords = line.split()
        passphrase_dict = Counter(passwords)
        if len(passwords) == len(passphrase_dict):
            valid_count = valid_count + 1
    return valid_count


if __name__ == '__main__':
    file = open('input.txt')
    print(solve(file))
