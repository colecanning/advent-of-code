from input_string import input_string
import string

items = input_string.split('\n')
print(items)


new_items = []
i = 0
while i+2 < len(items):
    new_items.append((items[i], items[i+1], items[i+2]))
    i += 3

items = new_items
print(items)

score = 0

"""
Get 3 elves worth
find duplicate in all 3
    keep each line as a list
    sort each
    iterate through and find duplicate. Only iterate the least one of the three
    base case is if all 3 match
"""
for (list_a, list_b, list_c) in items:
    # n log n
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    list_c = sorted(list_c)
    duplicate = None

    pa, pb, pc = 0, 0, 0
    while pa < len(list_a) and pb < len(list_b) and pc < len(list_c):
        ia = list_a[pa]
        ib = list_b[pb]
        ic = list_c[pc]

        # done
        if ia == ib and ib == ic:
            duplicate = ia
            break

        if ia == ib:
            if ic < ia:
                pc += 1
            else:
                pa += 1
                pb += 1
        elif ib == ic:
            if ia < ib:
                pa += 1
            else:
                pb += 1
                pc += 1
        elif ia == ic:
            if ib < ia:
                pb += 1
            else:
                pa += 1
                pc += 1
        else:
            # increment the min
            min_letter = min(ia, ib, ic)
            if ia == min_letter:
                pa += 1
            if ib == min_letter:
                pb += 1
            if ic == min_letter:
                pc += 1

    print(f'Dup: {duplicate}')
    if duplicate.isupper():
        score += 26
        duplicate = duplicate.lower()

    score += string.ascii_lowercase.index(duplicate) + 1


print(score)
