# operations.
def spin(programs, spin_arg):
    spin_arg = int(spin_arg)
    end = programs[-spin_arg::]
    front = programs[0:len(programs) - spin_arg]
    return end + front


def exchange(programs, index_a, index_b):
    index_a = int(index_a)
    index_b = int(index_b)
    output = programs[:]
    val_index_a = programs[index_a]
    val_index_b = programs[index_b]

    output[index_a] = val_index_b
    output[index_b] = val_index_a
    return output


def swap(programs, program_a, program_b):
    output = programs[:]
    index_program_a = output.index(program_a)
    index_program_b = output.index(program_b)

    output[index_program_a] = program_b
    output[index_program_b] = program_a
    return output


# function lookup dict.
function_dict = {
    's': spin,
    'x': exchange,
    'p': swap
}

# programs = ['a', 'b', 'c', 'd', 'e']

# step1 = spin(programs, 1)
# step2 = exchange(step1, 3, 4)
# step3 = swap(step2, 'e', 'b')

# programs = [
#     'a', 'b', 'c', 'd',
#     'e', 'f', 'g', 'h',
#     'i', 'j', 'k', 'l',
#     'm', 'n', 'o', 'p'
# ]

with open('./input.txt', 'r') as input:
    operations = input.read().split(',')
programs = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p']
original_programs = programs[:]
for i in range(0, 10):
    for operation_information in operations:
        operation_type = operation_information[0]
        operation_arguments = operation_information[1:].split('/')
        new_programs = function_dict[operation_type](programs, *operation_arguments)
        programs = new_programs
        # if programs == original_programs:
        #     print(i)

result = ''.join(new_programs)

print(result)


