def hamming_distance(s, t):
    result = 0

    for a, b in zip(s, t):
        if a != b:
            result += 1

    return result
    