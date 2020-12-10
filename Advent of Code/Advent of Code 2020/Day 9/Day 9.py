from itertools import combinations

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [int(n) for n in f.read().split("\n")]

def valid_number(number, preamble):
    return number in [sum(pair) for pair in combinations(preamble, 2)]

def part_1(numbers):
    preamble_size = 25

    for i in range(preamble_size, len(numbers)):
        if not valid_number(numbers[i], numbers[i - preamble_size:i]):
            return numbers[i]

def part_2(numbers):
    def contiguous_sets(numbers):
        n = len(numbers)
        indices = list(range(n + 1))

        for i, j in combinations(indices, 2):
            yield numbers[i:j]

    def find_set(number, numbers):
        for contiguous_set in contiguous_sets(numbers):
            if sum(contiguous_set) == number:
                return min(contiguous_set) + max(contiguous_set)

    preamble_size = 25
    
    for i in range(preamble_size, len(numbers)):
        if not valid_number(numbers[i], numbers[i - preamble_size:i]):
            return find_set(numbers[i], numbers[:i])

numbers = read_file()

print(f"Part 1: {part_1(numbers)}")
print(f"Part 2: {part_2(numbers)}")
