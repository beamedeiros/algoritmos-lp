soma = 0
n = 0

while True:
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    else:
        n +=1
    soma += x
    media = soma / n

print (f"Média: {media:.2f}")