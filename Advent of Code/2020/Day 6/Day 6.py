f = open("Day 6 - Input.txt", "r")

groups = f.read().split("\n\n")

def part_1():
    result = 0

    for group in groups:
        answers = set()

        for person in group:
            person = person.strip("\n")
            answers |= set(person)

        result += len(answers)

    print(result)

def part_2():
    result = 0

    for group in groups:
        size = group.count("\n") + 1
        group = group.replace("\n", "")
        answers = {x: group.count(x) for x in set(group)}  

        for answer in answers:
            if answers[answer] == size:
                result += 1

    print(result)

part_1()
part_2()
