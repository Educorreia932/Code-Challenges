f = open("rosalind_rna.txt", "r")

dna = f.read().strip()
rna = dna.replace("T", "U")

print(rna)
