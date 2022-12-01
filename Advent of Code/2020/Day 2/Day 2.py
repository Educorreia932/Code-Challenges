f = open("Day 2 - Input.txt", "r") 

passwords = f.read().split("\n") 

def part_1():
    result = 0

    for line in passwords:
        line = line.split(" ")
        interval = line[0].split("-")

        lower = int(interval[0])
        higher = int(interval[1])

        character = line[1][0]

        if lower <= line[2].count(character) <= higher:
            result += 1

    print(result)

def part_2():
    result = 0

    for line in passwords:
        line = line.split(" ")
        interval = line[0].split("-")

        lower = int(interval[0]) - 1
        higher = int(interval[1]) - 1

        character = line[1][0]
        line = line[-1]

        if line[lower] != line[higher] and character in (line[lower], line[higher]):
            result += 1

    print(result)
        
part_1()
part_2()
