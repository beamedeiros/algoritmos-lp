#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores
#podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: 
#equilátero, isósceles ou escaleno.

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a > b + c or b > a + c or c > a + b:
    print('Não forma um triângulo.')
elif a == b == c:
    print('Triângulo Equilátero.')
elif a == b or b == c or a == c:
    print('Triângulo Isóceles.')
else:
    print('Escaleno')