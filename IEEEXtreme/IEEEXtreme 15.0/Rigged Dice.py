games = int(input())

for g in range(games):
    rounds = int(input())

    dice_a = [0] * 7
    dice_b = [0] * 7

    alice_dice = dice_a
    bob_dice = dice_b

    alice_score = 0
    bob_score = 0

    for r in range(rounds):
        a, b = (int(e) for e in input().split())

        alice_dice[a] += 1
        bob_dice[b] += 1

        alice_score += a
        bob_score += b

        if alice_score != bob_score:
            alice_dice, bob_dice = bob_dice, alice_dice

    if dice_a[6] > dice_b[6]:
        print(1)
        
    else:
        print(2)
