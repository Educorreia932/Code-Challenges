f = open("Day 1 - Input.txt", "r") 

expenses = f.read().split("\n") 

def part_1():
    for i, l1 in enumerate(expenses):
        for l2 in expenses[i:]:
            l1 = int(l1)
            l2 = int(l2)

            if l1 + l2 == 2020:
                print(l1 * l2)

def part_2():
    for i, l1 in enumerate(expenses):
        for j, l2 in enumerate(expenses[i:]):
            for l3 in expenses[j:]:
                l1 = int(l1)
                l2 = int(l2)
                l3 = int(l3)

                if l1 + l2 + l3 == 2020:
                    print(l1 * l2 * l3)

part_1()
part_2()
