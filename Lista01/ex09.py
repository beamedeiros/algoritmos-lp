#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input("Digite a quatidade de km percorrido: "))
d = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

c = d * 60
kmr = km * 0.15
total = c + kmr

print(f"Preço a ser pago: {total:.2f}")