f = open("day01_input1.txt")
input = f.readlines()

elf_calories = []
elf_count = 0
subtotal = 0
max_calories = 0
max_elf = 0
for line in input:
    if len(line.strip())==0:
        elf_calories.append(subtotal)
        elf_count += 1
        #print(f"Elf {elf_count} carries {subtotal}")
        if subtotal >= max_calories:
            max_calories = subtotal
            max_elf = elf_count
            print(f"New best count: {max_calories} by elf {max_elf}")
        subtotal = 0
    else:
        subtotal += int(line.strip())

print(f"Part One answer: {max_calories} by elf {max_elf}")

elf_calories.sort(reverse=True)   # sort in descending order
top_3_total = elf_calories[0] + elf_calories[1] + elf_calories[2]
print(f"Part Two answer: total from top three elves is {top_3_total}")