import itertools

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [int(n) for n in f.read().split(",")]

def sequence(starting_numbers):
    seen = {n:i for i, n in enumerate(starting_numbers)}
    value = 0
    i = len(starting_numbers)

    for n in starting_numbers:
        yield n

    while True:
        yield value

        last = {value: i}
        value = i - seen.get(value, i)
        seen.update(last)

        i += 1

def part_1(starting_numbers):
    return list(itertools.islice(sequence(starting_numbers), 2020))[-1]

def part_2(starting_numbers):
    return list(itertools.islice(sequence(starting_numbers), 30000000))[-1]

starting_numbers = read_file()

print(f"Part 1: {part_1(starting_numbers)}")
print(f"Part 2: {part_2(starting_numbers)}")
