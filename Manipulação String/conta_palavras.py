with open("texto.txt", "w") as f:
    f.write("Python é uma linguagem de programação poderosa e fácil de aprender")

with open("texto.txt", "r") as f:
    conteudo = f.read()

palavras = conteudo.split()
print(f"Número de palavras no arquivo: {len(palavras)}")
