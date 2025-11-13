from pathlib import Path
from hashlib import md5

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().rstrip()

for i in range(10000000):
    h = md5((data + str(i)).encode()).hexdigest()
    if h[:5] == "00000":
        output = i
        break

print("Part one:", output)
