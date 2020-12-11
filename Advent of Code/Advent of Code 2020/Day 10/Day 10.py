def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [int(n) for n in f.read().split("\n")]

def part_1(adapters):
    differences = [y - x for x, y in zip(adapters[:-1], adapters[1:])]

    return differences.count(1) * differences.count(3)


def part_2(adapters):
    i = 0
    size = adapters[-1] + 1
    counter = [0] * size
    counter[0] = 1

    for adapter in adapters:
        for i in range(1, 4):
            if adapter - i >= 0:
                counter[adapter] += counter[adapter - i]

    return counter[-1]

adapters = read_file()

adapters.sort()
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)

print(f"Part 1: {part_1(adapters)}")
print(f"Part 2: {part_2(adapters)}")
