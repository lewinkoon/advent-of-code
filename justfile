default:
    @just --list --unsorted

# Run a specific year and day
run year day="01" part="p1":
    @echo "Running Advent of Code {{year}}, day {{day}}, part {{part}}"
    uv run {{year}}/{{day}}/{{part}}.py