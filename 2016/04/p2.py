from pathlib import Path
import re

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.readlines()

output = 0

for line in data:
    room = line.split("-")
    encrypted = "-".join(room[:-1])
    id = re.search(r"\d{3}", room[-1]).group()

    msg = ""
    for char in encrypted:
        if char.isalpha():
            msg += chr((ord(char) - ord("a") + int(id)) % 26 + ord("a"))
        else:
            msg += " "

    if "northpole" in msg:
        output = id
        break

print("Part two:", output)
