from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
print(f"Reading input from: {input_path}")

with open(input_path, "r") as file:
    res = 0
    position = 50
    print(f"Starting position: {position}\n")
    for line in file:
        direction = line[0]
        rotation = int(line[1:])
        print(f"Processing move: {line.strip()}")

        if direction == 'L':
            position = (position - rotation) % 100
        elif direction == 'R':
            position = (position + rotation) % 100
            
        print(f"New position: {position}\n")
        
        if position == 0:
            res += 1
        
print("Part One:", res)
