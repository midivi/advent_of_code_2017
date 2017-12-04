from collections import Counter


def solve(input_file):
    valid_count = 0
    for line in input_file:
        passwords = line.split()
        sorted_passwords = list(map(lambda x: ''.join(sorted(x)), passwords))
        passphrase_dict = Counter(sorted_passwords)
        if len(sorted_passwords) == len(passphrase_dict):
            valid_count = valid_count + 1
    return valid_count


if __name__ == '__main__':
    file = open('input.txt')
    print(solve(file))
