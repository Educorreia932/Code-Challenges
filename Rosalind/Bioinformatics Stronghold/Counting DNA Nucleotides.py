f = open("rosalind_dna.txt", "r")

sequence = f.read().strip()
frequencies = {c:sequence.count(c) for c in set(sequence)}

print(f"{frequencies['A']} {frequencies['G']} {frequencies['G']} {frequencies['T']}")
