def solution(l):
    return sorted(l, key=lambda x: [int(n) for n in x.split(".")])
    