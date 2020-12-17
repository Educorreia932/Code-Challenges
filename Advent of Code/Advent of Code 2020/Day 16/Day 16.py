from rich import print
import re

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        f = f.read().split("\n\n")

        ticket_fields = []

        for field in f[0].split("\n"):
            groups = re.match(r'(?:[^:]+): (\S+)\s* or (\S+)\s*', field).groups()

            ranges = [[int(n) for n in group.split("-")] for group in groups]
            ticket_fields.append(ranges)

        your_ticket = [int(n) for n in f[1].split("\n")[1].split(",")]
        nearby_tickets = [[int(n) for n in ticket.split(",")] for ticket in f[2].split("\n")[1:]]

        document = [ticket_fields, your_ticket, nearby_tickets]

    return document

def check_ticket(ticket, fields):
    result = []

    for value in ticket:
        correct = False

        for field in fields:
            if field[0][0] <= value <= field[0][1] or field[1][0] <= value <= field[1][1]:
                correct = True

        if not correct:
            result.append(value)

    return result

def part_1(document):
    result = 0
    
    for ticket in document[2]:
        errors = check_ticket(ticket, document[0])
        result += sum(errors)

    return result

def part_2(document):
    pass

document = read_file()

print(f"Part 1: {part_1(document)}")
# print(f"Part 2: {part_2(document)}")