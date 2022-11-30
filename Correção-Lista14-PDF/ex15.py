a = float(input("Digite um número: "))

if a > 10 and a % 6 == 3:
    print('A', end = '')
elif a > 10 and a < 20:
    print('B', end = '')
else:
    print('C', end = '')