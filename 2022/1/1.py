from input import input_diet
from functools import reduce

input_diets = input_diet.split('\n\n')
elf_diets = [i.split('\n') for i in input_diets]
elf_diets = [[int(i) for i in elf_diet] for elf_diet in elf_diets]
elf_diets_sum = [reduce(lambda a, b: a + b, elf_diet) for elf_diet in elf_diets]

# Answer 1
print(max(elf_diets_sum))

elf_diets_sum = sorted(elf_diets_sum, reverse=True)
print(elf_diets_sum[:3])

# Answer 2
print(sum(elf_diets_sum[:3]))
