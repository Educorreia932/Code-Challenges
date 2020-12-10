def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [int(n) for n in f.read().split("\n")]

def part_1():


numbers = read_file()

print(f"Part 1: {part_1(numbers)}")
print(f"Part 2: {part_2(numbers)}")