# contadora
n = 1

# acumuladora
soma = 0

while n <= 10:
    x = int(input(f'{n} número: '))
    soma += x
    n += 1
    media = soma / 10

print(f"Média: {media:.2f}")