from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().splitlines()

n = 0
ll = list()
la = list()

for line in data:
    ll.append(list(map(int, line.lstrip().split())))

for i in range(len(ll) // 3):
    for j in range(3):
        ln = [ll[i * 3][j], ll[i * 3 + 1][j], ll[i * 3 + 2][j]]
        ln.sort()
        la.append(ln)

for l in la:
    if l[0] + l[1] > l[2]:
        n += 1

print("Part two:", n)
