T = int(input()) # Number of test cases

for i in range(T):
    M, N, K = [int(x) for x in input().split((" "))]

    incorrect = [] # Rooms with incorrect wiring in each floor

    for floor in range(M):
        incorrect.append(N - int(input()))

    incorrect.sort(reverse=True)
    counter = 0
    index = 0

    while K > 0:
        counter += incorrect[index]
        index += 1
        K -= 1

    for j in range(index, M):
        counter += N - incorrect[j]

    print(counter)
    