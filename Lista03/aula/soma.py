# contadora
n = 1

# acumuladora
soma = 0

while n <= 10:
    x = int(input(f'{n} número: '))
    soma += x
    n += 1

print(f"Soma: {soma}")