def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [[int(n) for n in deck.split("\n")[1:]] for deck in f.read().split("\n\n")]

def part_1(decks):
    while decks[0] and decks[1]:
        play_1 = decks[0][0]
        play_2 = decks[1][0]

        winner = 0 if play_1 > play_2 else 1
        loser = 0 if winner == 1 else 1

        decks[winner] += [decks[winner].pop(0), decks[loser].pop(0)]

    decks.remove([])
    score = sum((i + 1) * n for i, n in enumerate(decks[0][::-1]))

    return score

decks = read_file()

print(f"Part 1: {part_1(decks)}")
# print(f"Part 2: {part_2()}")
