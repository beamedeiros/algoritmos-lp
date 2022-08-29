#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo - 
#se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o 
#salário líquido. 
#Observe que Salário Bruto - Descontos = Salário Líquido. 
#Calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#a. + Salário Bruto : R$ 
#b. - IR (11%) : R$ 
#c. - INSS (8%) : R$ 
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

v = float(input('Valor por hora: '))
h = int(input('Horas tralhadas: '))

b = v * h
ir = b * 0.11
inss = b * 0.08
sind = b * 0.05
l = b - ir - inss - sind

print (f'+ Salário Bruto:\t\t R$ {b:.2f}')
print (f'-IR:\t\t\t R$ {ir:.2f}')
print (f'-INSS:\t\t\t R$ {inss:.2f}')
print (f'-Sindicato:\t\t R$ {sind:.2f}')
print (f'-Salário Líquido:\t R$ {l:.2f}')