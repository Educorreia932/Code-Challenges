from rich import print
import re

f = open("Day 4 - Input.txt", "r")

fields = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
)

passports = f.read().split("\n\n")

def part_1():
    result = 0

    for passport in passports:
        passport = "".join(passport)

        for field in fields:
            if field not in passport:
                break

        else:
            result += 1

    print(result)

def part_2():
    def check_year(year, lower, higher):
        if not year.isnumeric():
            return False

        year = int(year)
        
        if lower <= year <= higher:
            return True

        return False

    def check_height(height):
        if len(height) < 4:
            return False

        unit = height[-2:]

        if not height[:-2].isnumeric():
            return False

        height = int(height[:-2])

        if unit == "cm" and 150 <= height <= 193:
            return True

        if unit == "in" and 59 <= height <= 76:
            return True

        return False

    def check_hair_color(hair_color):
        return re.search(r"#[0-9a-f]{6}", hair_color) 

    def check_eye_color(eye_color):
        return eye_color in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    def check_passport(passport):
        return passport.isnumeric() and len(passport) == 9

    result = 0

    for passport in passports:
        entries = passport.replace("\n", " ").split(" ")

        if False in (x in passport for x in fields):
            continue

        for entry in entries:
            entry = entry.split(":")

            if entry[0] == "byr" and not check_year(entry[1], 1920, 2002):
                break

            if entry[0] == "iyr" and not check_year(entry[1], 2010, 2020):
                break

            if entry[0] == "eyr" and not check_year(entry[1], 2020, 2030):
                break

            if entry[0] == "hgt" and not check_height(entry[1]):
                break

            if entry[0] == "hcl" and not check_hair_color(entry[1]):
                break

            if entry[0] == "ecl" and not check_eye_color(entry[1]):
                break

            if entry[0] == "pid" and not check_passport(entry[1]):
                break

        else:
            result += 1

    print(result)

part_1()
part_2()
