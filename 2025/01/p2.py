from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
print(f"Reading input from: {input_path}")

with open(input_path, "r") as file:
    count = 0
    position = 50
    for line in file:
        direction = line[0]
        rotation = int(line[1:])
        print(f"Processing move: {line.strip()}")

        old_position = position
        new_position = (position + (rotation if direction == "R" else -rotation)) % 100
        print(f"Old position: {old_position}")
        print(f"Intended new position: {new_position}")

        # Count how many times the dial points at 0 during this rotation
        if direction == "L":
            # Rotating left (counter-clockwise): position decreases
            # Full rotations: each full 100-step rotation passes through 0
            full_rotations = rotation // 100
            count += full_rotations
            remaining = rotation % 100
            print(
                f"Full left rotations: {full_rotations}, Remaining steps: {remaining}"
            )

            # Check if we pass 0 in the remaining steps
            if (old_position - remaining) <= 0 and old_position != 0:
                count += 1
                print("Passed 0 during left rotation")

        elif direction == "R":
            # Rotating right (clockwise): position increases
            full_rotations = rotation // 100
            remaining = rotation % 100
            count += full_rotations
            print(
                f"Full left rotations: {full_rotations}, Remaining steps: {remaining}"
            )
            # Check if we pass 0 in the remaining steps
            if (old_position + remaining) >= 100 and old_position != 0:
                count += 1
                print("Passed 0 during right rotation")

        position = new_position
        print(f"New position: {position}")
        print(f"Count so far: {count}\n")

print("Part Two:", count)
