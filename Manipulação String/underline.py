with open("texto_espacos.txt", "w") as f:
    f.write("Olá mundo Python é incrível")

with open("texto_espacos.txt", "r") as f:
    conteudo = f.read()

novo_conteudo = conteudo.replace(" ", "_")
print(f"Original:   {conteudo}")
print(f"Modificado: {novo_conteudo}")

with open("texto_underline.txt", "w") as f:
    f.write(novo_conteudo)
