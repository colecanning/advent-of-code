from input_string import input_string
import string

items = input_string.split('\n')
print(items)

items = [(i[:int(len(i)/2)], i[int(len(i)/2):]) for i in items]
print(items)

print(string.ascii_lowercase.index('b'))
score = 0

"""
split in half
find duplicate
    sort. (n log n)
    search (n)
score dup
sum scores
"""
# O (N (n log n))
for (list_a, list_b) in items:
    print(list_a)
    print(list_b)

    # n log n
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    duplicate = ''

    # n
    pa, pb = 0, 0
    while pa < len(list_a) and pb < len(list_b):
        ia = list_a[pa]
        ib = list_b[pb]

        if ia == ib:
            duplicate = ia
            break

        if pb > len(list_b) or ia < ib:
            pa += 1
        elif pa < len(list_a) or ib < ia:
            pb += 1

    if duplicate.isupper():
        score += 26
        duplicate = duplicate.lower()

    score += string.ascii_lowercase.index(duplicate) + 1

    print(f'Dup: {duplicate}')

print(score)
