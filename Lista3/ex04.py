# A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o
# seu númerode Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.

x = int(input("Digite um número: "))

a, b = 1, 1
y = 1

while y <= x - 2:
    a, b = b, a + b
    y += 1

print (b)