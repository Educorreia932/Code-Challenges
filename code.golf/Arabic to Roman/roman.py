import sys

for number in map(int, sys.argv[1:]):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    i = 12

    while number:
        print("I-IVV-IXX-XLL-XCC-CDD-CMM-"[i * 2:i * 2 + 2].replace("-", "") * (number // num[i]), end="")

        number %= num[i]

        i -= 1

    print()