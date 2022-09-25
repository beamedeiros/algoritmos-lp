notas = [6, 7, 8, 9 , 10]
soma = 0 
c = 0

while c < len(notas):
    soma = soma + notas[c]
    c += 1

media = soma/len(notas)
print(f"Média: {media}")