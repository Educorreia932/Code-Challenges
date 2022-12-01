f = open("Day 5 - Input.txt", "r")

boarding_passes = f.read().split("\n")

def get_seats(): 
    return [
        int(boarding_pass.
            replace("F", "0").
            replace("B", "1").
            replace("L", "0").
            replace("R", "1"), 2) 
        for boarding_pass in boarding_passes]

def part_1():
    print(max(get_seats()))

def part_2():
    seats = get_seats()
    seats.sort()

    for seat in range(seats[0], seats[-1] + 1):
        if seat not in seats:
            print(seat)

part_1()
part_2()
