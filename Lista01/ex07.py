#Converta uma temperatura digitada em Celsius para Fahrenheit.
#F = 9*C/5 + 32

c = float(input("Digite a temperatura em Celcius: "))

f = (9*c) / 5+32

print(f"A temperatura convertida para Fahreinheit é: {f:.2f}")