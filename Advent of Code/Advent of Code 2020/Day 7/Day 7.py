import re

f = open("Day 7 - Input.txt", "r")

rules = f.read().split("\n")

def parse_input():
    bags = {}

    for rule in rules:
        rule = rule.split(" bags contain ")
        bag_color = rule[0]
        contained_bags = []

        for contained_bag in rule[1].split(","):
            contained_bag = re.sub(r"^\s+|\sbags?|no other|\.", "", contained_bag)

            if contained_bag == "":
                continue

            contained_bag = contained_bag.split(" ", 1)
            contained_bags.append([int(contained_bag[0]), contained_bag[1]])

        bags[bag_color] = contained_bags
    
    return bags

def part_1():
    def contains_bag(bags, start, end):
        for contained_bag in bags[start]:
            if contains_bag(bags, contained_bag[1], end):
                return True

        return start == end

    result = 0
    bags = parse_input()

    for bag in bags:
        if contains_bag(bags, bag, "shiny gold") and bag != "shiny gold":
            result += 1

    print(result)

def part_2():
    def count_bags(bags, bag_color):
        count = 0

        for contained_bag in bags[bag_color]:
            count += contained_bag[0] + contained_bag[0] * count_bags(bags, contained_bag[1])
        
        return count

    bags = parse_input()
    print(count_bags(bags, "shiny gold"))

part_1() # 139
part_2() # 58175
