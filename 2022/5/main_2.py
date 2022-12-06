from input_string import input_string_test_stack, input_string_test_moves, input_string_real_stack, \
    input_string_real_moves
from collections import defaultdict


# # toggle test or real
# input_test_stack = input_string_test_stack
# input_string_moves = input_string_test_moves

input_test_stack = input_string_real_stack
input_string_moves = input_string_real_moves

input_test_stack = input_test_stack.replace('    ', ' ')

items = input_test_stack.split('\n')

items = [i.replace('[', '').replace(']', '').split(' ') for i in items]

num_stacks = len(items[0])

stacks = [[] for i in range(num_stacks)]

for row in reversed(items):
    for index, col_val in enumerate(row):
        if col_val:
            stacks[index].append(col_val)

print(stacks)

print(input_string_moves)

input_moves = input_string_moves.split('\n')
input_moves = [i.split(' ') for i in input_moves]
print(input_moves)

for move in input_moves:
    num = int(move[1])
    source = int(move[3]) - 1
    target = int(move[5]) - 1

    new_stack = []
    for i in range(num):
        popped = stacks[source].pop()
        new_stack.append(popped)
    for item in reversed(new_stack):
        stacks[target].append(item)

print(stacks)

final_word = ''

for stack in stacks:
    final_word += stack[-1]

print(final_word)
