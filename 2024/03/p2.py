from pathlib import Path
from re import findall

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read()

total = 0
enabled = True
for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        total += x * enabled

print("Part Two:", total)
