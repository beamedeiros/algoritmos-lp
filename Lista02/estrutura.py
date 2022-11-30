t = int(input("Digite quantos minutos você ficou em ligação: "))

if t < 200:
	p = 0.2

else:
	if t <= 400:
		p = 0.18
	else:
		p = 0.15

print(f"R${p:.2f}")