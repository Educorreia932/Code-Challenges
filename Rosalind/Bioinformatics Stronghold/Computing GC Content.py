def gc_content(string):
    if len(string) == 0:
        return 0

    return (string.count("G") + string.count("C")) / len(string)

f = open("input/rosalind_gc.txt", "r")

result = 0
sequences = {}

for line in f.readlines():
    line = line.strip()

    if line[0] == ">":
        current_id = line[1:]
        sequences[current_id] = ""

    else:
        sequences[current_id] += line

sequences =  {k: gc_content(v) for k, v in sequences.items()}

greatest_content_id = max(sequences, key=sequences.get)
greatest_content = sequences[greatest_content_id] * 100

print(f"{greatest_content_id}\n{greatest_content}")