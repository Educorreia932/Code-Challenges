def complement(dna):
    return dna[::-1] \
        .replace("A", "t") \
        .replace("C", "g") \
        .replace("G", "C") \
        .replace("T", "A") \
        .upper()
