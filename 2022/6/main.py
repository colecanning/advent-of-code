from input_string import real_input_string

test_input_string = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

# input_string = test_input_string
input_string = real_input_string

print(test_input_string)
buffer_length = 14
answer = None

for index, letter in enumerate(input_string):
    start = index
    encountered_letters = set()
    encountered_letters.add(letter)
    match_count = 0
    print(letter)
    for i in range(buffer_length-1):
        real_index = index + i + 1
        if real_index < len(input_string):
            new_letter = input_string[real_index]
            print(f'--{input_string[real_index]}')

            if new_letter in encountered_letters:
                break
            else:
                match_count += 1
                encountered_letters.add(new_letter)
        else:
            break
    if match_count == buffer_length-1:
        answer = index + buffer_length
        break

print(answer)

