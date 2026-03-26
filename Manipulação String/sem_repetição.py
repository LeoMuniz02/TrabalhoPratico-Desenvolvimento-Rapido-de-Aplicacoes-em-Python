with open("frases.txt", "w") as f:
    f.write("futebol tequila bola futebol torcida bola goleiro")

with open("frases.txt", "r") as f:
    frase = f.read().strip()

lista_sem_repeticao = []
for palavra in frase.split():
    if palavra not in lista_sem_repeticao:
        lista_sem_repeticao.append(palavra)

print(f"Frase original: {frase}")
print(f"Lista sem repetição: {lista_sem_repeticao}")
