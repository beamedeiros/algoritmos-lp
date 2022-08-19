#Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

mer = float(input("Digite o preço da mercadoria: R$"))
p = int(input("Digite a porcentagem do desconto: "))

d = mer * (p/100)
pag = mer - d

print(f"O valor do desconto é: R${d:.2f}")
print(f"O valor a ser pago é: R${pag:.2f}")
