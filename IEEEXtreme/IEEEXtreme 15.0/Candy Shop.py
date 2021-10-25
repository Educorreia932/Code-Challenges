from copy import deepcopy


def bfs(candies, target, current):
    result = 0

    if current == target:
        return 1

    if current > target:
        return 0

    for i in range(len(candies)):
        bags, quantity = candies[i]

        if bags == 0:
            continue

        candies_copy = deepcopy(candies)
        candies_copy[i][0] -= 1

        current += quantity

        result += bfs(candies_copy, target, current)

    return result


N, K = (int(x) for x in input().split())

candies = []

for _ in range(N):
    A, B = (int(x) for x in input().split())

    candies.append([A, B])

result = bfs(candies, K, 0)

print(result)
