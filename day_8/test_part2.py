"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

"""
from collections import Counter

OP_DICT = {
    'inc': 1,
    'dec': -1,
}


def solve(input):
    register = Counter()
    max_value = 0
    for line in input:
        target_register, op, op_value, _ , left_side, comparison, right_side = line.split()
        exec_string = """if register[\'{left_side}\'] {comparison} {right_side}: register[\'{target_register}\'] = register[\'{target_register}\'] + OP_DICT[\'{op}\'] * {op_value} """.format(
            left_side=left_side, comparison=comparison, right_side=right_side, target_register=target_register, op=op, op_value=op_value
        )
        exec(exec_string)
        if register[target_register] > max_value:
            max_value = register[target_register]
    return max_value


if __name__ == "__main__":
    input = open('input.txt')
    print(solve(input))


def test_solve():
    test_input = open("test_input.txt")
    solve(test_input) == 10
