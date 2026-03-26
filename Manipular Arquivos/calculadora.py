num1 = int(input("Primeiro número inteiro: "))
num2 = int(input("Segundo número inteiro: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)"

with open("calculadora.txt", "w") as f:
    f.write(f"Número 1: {num1}\n")
    f.write(f"Número 2: {num2}\n")
    f.write(f"Soma: {soma}\n")
    f.write(f"Subtração: {subtracao}\n")
    f.write(f"Multiplicação: {multiplicacao}\n")
    f.write(f"Divisão: {divisao}\n")

print("Arquivo 'calculadora.txt' criado!")
