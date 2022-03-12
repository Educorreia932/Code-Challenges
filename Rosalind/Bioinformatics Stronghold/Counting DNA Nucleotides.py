def nucleotides_frequencies(sequence):
    return {c:sequence.count(c) for c in set(sequence)}
