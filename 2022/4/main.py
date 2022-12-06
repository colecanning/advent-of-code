from input_string import input_string_test, input_string_real

# toggle test or real
# input_string = input_string_test
input_string = input_string_real


items = input_string.split('\n')
print(items)

items = [i.split(',') for i in items]
print(items)

# solution 2
score = 0
for item in items:
    raw_i_1 = item[0]
    raw_i_2 = item[1]
    bounds_1 = raw_i_1.split('-')
    bounds_2 = raw_i_2.split('-')
    min_1 = int(bounds_1[0])
    max_1 = int(bounds_1[1])
    min_2 = int(bounds_2[0])
    max_2 = int(bounds_2[1])

    if (max_2 >= min_1 and max_2 <= max_1) \
        or (max_1 >= min_2 and max_1 <= max_2) \
        or (min_1 >= min_2 and min_1 <= max_2) \
        or (min_2 >= min_1 and min_2 <= max_1):
        score += 1

print(score)


# # solution 1
# score = 0
# for item in items:
#     raw_i_1 = item[0]
#     raw_i_2 = item[1]
#     bounds_1 = raw_i_1.split('-')
#     bounds_2 = raw_i_2.split('-')
#     min_1 = int(bounds_1[0])
#     max_1 = int(bounds_1[1])
#     min_2 = int(bounds_2[0])
#     max_2 = int(bounds_2[1])
#
#     if (min_1 <= min_2 and max_1 >= max_2) or (min_2 <= min_1 and max_2 >= max_1):
#         score += 1
#
# print(score)

