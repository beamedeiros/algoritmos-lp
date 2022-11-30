#Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro,
#calcule quantos dias de vida um fumante perderá. Exiba o total de dias

qtd = int(input("Qual a quatidade de cigarros fumados por dia? "))
a = int(input("Por quantos anos já fumou? "))

t = a * 365 * qtd
d = (24 * 60) / 10
# se ele perde 10min (1440 / 10)
p = t / d

print(f"O fumante perdeu: {p:.1f} dia(s) de vida.")


