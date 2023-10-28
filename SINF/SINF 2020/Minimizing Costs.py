D = [int(x) for x in input().split(" ")]
R = [int(x) for x in input().split(" ")]

optimal_costs = [0 for x in range(len(D))]
optimal_costs[0] = R[0]

def optimal_cost(index):
    if index < 0:
        return 0

    if optimal_costs[index] != 0:
        return optimal_costs[index]

    mincost = optimal_cost(index - 1) + R[0]

    # Try to find a lower cost within three days
    for i in range(1, 4):
        if i > index or D[index] - D[index - i] >= 3:
            break

        next_cost = optimal_cost(index - i - 1) + R[1]

        if next_cost < mincost:
            mincost = next_cost

    # Try to find a lower cost within a week
    for i in range(1, 8):
        if i > index or D[index] - D[index - i] >= 7:
            break

        next_cost = optimal_cost(index - i - 1) + R[2]

        if next_cost < mincost:
            mincost = next_cost

    optimal_costs[index] = mincost

    return mincost

optimal_cost(len(D) - 1)

print(optimal_costs[-1])
