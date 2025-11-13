from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().rstrip().split(", ")

position = 0 + 0j
direction = 0 + 1j

for step in data:
    if step[0] == "L":
        direction *= 1j
    else:
        direction *= -1j

    length = int(step[1:])

    for _ in range(0, length):
        position += direction

res = int(abs(position.real) + abs(position.imag))
print("Part one:", res)
