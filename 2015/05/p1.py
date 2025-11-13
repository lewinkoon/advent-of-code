import re
from pathlib import Path


def countVowels(str):
    vowels = "aeiou"
    res = sum(str.count(vowel) for vowel in vowels)
    return res > 2


def countDuplicates(str):
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            return True

    return False


def checkSubtrings(str):
    substrings = ["ab", "cd", "pq", "xy"]
    for substr in substrings:
        if substr in str:
            return False

    return True


input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.readlines()

output = 0

for string in data:
    a = countVowels(string)
    b = countDuplicates(string)
    c = checkSubtrings(string)

    if a and b and c:
        output += 1

print("Part one:", output)
