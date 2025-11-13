import re
from pathlib import Path


def repeatingPairs(str):
    pattern = r"(\w\w)(?=.*\1)"
    return bool(re.search(pattern, str))


def letterBetween(str):
    pattern = r"(\w)(\w)\1"
    return bool(re.search(pattern, str))


input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.readlines()

output = 0

for string in data:
    a = repeatingPairs(string)
    b = letterBetween(string)

    if a and b:
        output += 1

print("Part two:", output)
