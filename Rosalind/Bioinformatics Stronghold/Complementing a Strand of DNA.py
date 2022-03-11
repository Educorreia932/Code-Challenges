f = open("input/rosalind_revc.txt", "r")

dna = f.read().strip()
complement = dna[::-1] \
    .replace("A", "t") \
    .replace("C", "g") \
    .replace("G", "C") \
    .replace("T", "A") \
    .upper()

print(complement)
