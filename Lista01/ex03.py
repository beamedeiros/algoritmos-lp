#Escreva um programa que leia a quantidade de dias, horas,
#minutos e segundos do usuário. Calcule o total em segundos.

d = int(input("Digite os dias: "))
h = int(input("Digite as horas: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

total = d*24*60*60 + h*60*60 + m*60 + s

print("O total em segundos é: ", total)
