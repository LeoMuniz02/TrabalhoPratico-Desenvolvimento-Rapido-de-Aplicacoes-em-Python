with open("dna.txt", "w") as f:
    f.write("AATCTGCAC")

with open("dna.txt", "r") as f:
    cadeia = f.read().strip()

inversa = cadeia[::-1]
print(f"Entrada: {cadeia}")
print(f"Saída:   {inversa}")

with open("dna_inverso.txt", "w") as f:
    f.write(f"Entrada: {cadeia}\n")
    f.write(f"Saída: {inversa}\n")
