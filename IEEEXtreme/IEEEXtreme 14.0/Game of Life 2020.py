from copy import deepcopy

board = []

rules = input().split(";")

for i in range(2):
    rules[i]= [j for j in range(5) if rules[i][j] == "1"]

N, M = (int(x) for x in input().split(" "))

def cell_state(i, j):
    cell = int(board[i][j])

    neighbors = [
        board[(i - 1) % N][k], # Up
        board[(i + 1) % N][k], # Down
        board[i][(k - 1) % N], # Left
        board[i][(k + 1) % N], # Right
    ]

    alive = neighbors.count("1")

    for i in rules[cell]:
        if i == alive:
            return "1"

    return "0" 

for i in range(N):
    line = input()

    board.append(list(line))

# Generations
for i in range(M):
    generation = [["0" for i in range(N)] for j in range(N)]

    for j in range(N):
        for k in range(N):
            generation[j][k] = cell_state(j, k)

    board = deepcopy(generation)

for line in board:
    print("".join(line))
