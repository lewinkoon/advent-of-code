from collections import Counter
from pathlib import Path
import re


def mostFrequent(lst, n):
    counter = Counter(lst)
    common = counter.most_common()
    items = sorted(common, key=lambda x: (-x[1], x[0]))
    return "".join([item for item, _ in items[:5]])


input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().splitlines()

output = 0

for line in data:
    room = line.split("-")
    name = "".join(room[:-1])

    checksum = re.search(r"\[([a-zA-Z]+)\]", room[-1]).group(1)
    id = re.search(r"\d{3}", room[-1]).group()
    res = mostFrequent(name, 5)

    if res == checksum:
        output += int(id)

print("Part one:", output)
