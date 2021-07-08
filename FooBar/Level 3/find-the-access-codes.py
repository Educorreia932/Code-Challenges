def solution(l):
    result = 0
    doubles = [0] * len(l)

    for i in range(1, len(l) - 1):
        li = l[i]

        for j in range(i):
            lj = l[j]

            if li % lj == 0:
                doubles[i] += 1

    for i in range(2, len(l)):
        li = l[i]

        for j in range(1, i):
            lj = l[j]

            if li % lj == 0:
                result += doubles[j]

    return result
