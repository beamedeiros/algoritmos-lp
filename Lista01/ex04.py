#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

sal = float(input("Digite o seu salário: R$"))
p = int(input("Digite a porcentagem de aumento: "))

a  = sal * (p/100)
novo = sal + a

print(f"O valor do seu aumento é: R${a:.2f}")
print(f"O valor do seu novo salário é: R${novo:.2f}")