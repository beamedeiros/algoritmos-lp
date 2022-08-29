#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
#da área aser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#Obs. : somente são vendidos um número inteiro de latas.

m = int(input('Metros: '))

if m % 54 == 0:
  l = m / 54
else:
  l = int(m / 54) + 1

val = l * 80

print (f'Quantidade de {l} latas de tinta.')
print (f'Total: R$ {val:.2f}')