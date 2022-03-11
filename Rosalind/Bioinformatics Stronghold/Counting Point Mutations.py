def hamming_distance(s, t):
    result = 0

    for a, b in zip(s, t):
        if a != b:
            result += 1

    return result

f = open("input/rosalind_hamm.txt", "r")

s, t = f.readlines()

print(hamming_distance(s, t))
