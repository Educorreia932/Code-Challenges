def card_value(card):
    return "23456789TJQKA".index(card) + 2

def play_game(player_1, player_2):
    draw_count = 0

    while True:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if card_1 > card_2:
            player_1.append(card_2)
            draw_count = 0

        elif card_1 < card_2:
            player_2.append(card_1)
            draw_count = 0

        else:
            player_1.append(card_1)
            player_2.append(card_2)

            draw_count += 1 

        if len(player_1) == 0:
            return "player 2"
        
        elif len(player_2) == 0:
            return "player 1"
        
        elif draw_count == len(player_1) == len(player_2) or draw_count > max(len(player_1), len(player_2)):
            return "draw"

n = int(input())

for i in range(n):
    player_1 = [card_value(x) for x in input().split()]
    player_2 = [card_value(x) for x in input().split()]

    print(play_game(player_1, player_2))
