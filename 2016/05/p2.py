import hashlib
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.readline().rstrip()

pwd = [None] * 8
counter = 0

for i in range(100000000):
    id = data + str(i)
    hash = hashlib.md5(id.encode()).hexdigest()

    if hash[:5] == "00000" and hash[5].isdigit():
        print(id, hash)
        index = int(hash[5])
        char = hash[6]

        if index < len(pwd):
            if pwd[index] == None:
                counter += 1
                pwd[index] = char

    if counter == 8:
        break

output = "".join(pwd)

print("Part two:", output)
