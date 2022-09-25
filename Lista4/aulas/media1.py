notas = []
c = 1

# contador normal
while c <= 4:
    # adiciona nota no final até ter 4
    notas.append(float(input("Nota: ")))
    c +=1

soma = c = 0

# acessar cada elemento da lista (primeiro elemento é sempre 0)
while c <= 3:
    soma = soma + notas[c]
    c += 1

print(f"Média {notas} é {soma/4:.1f}")