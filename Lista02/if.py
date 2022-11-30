v = float(input("Digite a velocidade em km/h: "))

if v > 110:
	m = ( v - 110 ) * 5
	print(f"Sua multa, é de R${m}")
else:
	print("Você não foi multado")