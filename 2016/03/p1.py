from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().splitlines()

n = 0

for line in data:
    line = line.strip().split()
    vals = sorted([int(x) for x in line])
    if vals[0] + vals[1] > vals[2]:
        n += 1

print("Part one:", n)
