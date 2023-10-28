from math import ceil

T = int(input()) # Number of test cases

def lario_wins(LH, LD, BH, BD, D, H, m, n):
    a = ceil((LH + n * H) / BD)    # Rounds before dying
    b = ceil(BH / (LD + m * D))    # Rounds to kill Bowser

    return a >= b

for t in range(T):
    LH, LD = (int(x) for x in input().split())
    BH, BD = (int(x) for x in input().split())
    C, D, H = (int(x) for x in input().split())

    victory = "NO"

    for m in range(C + 1):
        n = C - m

        if lario_wins(LH, LD, BH, BD, D, H, m, n):
            victory = "YES"

            break

    print(victory)
