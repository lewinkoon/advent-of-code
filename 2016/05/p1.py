import hashlib
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.readline().rstrip()

pwd = ""
counter = 0

for i in range(100000000):
    id = data + str(i)
    hash = hashlib.md5(id.encode()).hexdigest()

    if hash[:5] == "00000":
        pwd += hash[5]
        counter += 1

        if counter == 8:
            break

print("Part one:", pwd)
