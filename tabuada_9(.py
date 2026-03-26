num = 9
tabuada = open('tabuada_9.txt', 'w', encoding='utf-8')
tabuada.write('Tabuada de 9\n')
for i in range(1, 11):
    result = num * i
    linhas = f"{num} x {i} = {result}\n"
    tabuada.write(linhas)
tabuada.close()