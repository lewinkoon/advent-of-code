from pathlib import Path
from re import findall

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read()

total = 0
for a, b in findall(r"mul\((\d+),(\d+)\)", data):
    x = int(a) * int(b)
    total += x

print("Part One:", total)
