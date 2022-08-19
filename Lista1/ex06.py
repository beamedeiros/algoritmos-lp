#Calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

d = float(input("Digite a distância (km): "))
v = float(input("Digite a velocidade média (km/h)"))

t = d/v

print(f"O tempo é de: {t:.2f}")