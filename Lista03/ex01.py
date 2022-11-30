# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

x = float(input("Digite uma nota entre 0 e 10: "))

while x < 0 or x > 10:
    print("Nota inválida!")
    x = float(input("Digite uma nota entre 0 e 10: "))