from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

list1 = []
list2 = []

with open(input_path, "r") as file:
    for line in file:
        values = line.split()
        if len(values) == 2:
            list1.append(int(values[0]))
            list2.append(int(values[1]))

counts = {num: list2.count(num) for num in list1}

res = 0
for left, right in zip(sorted(list1), sorted(list2)):
    count = list2.count(left)
    sim = left * count
    res += sim

print("Part Two:", res)
