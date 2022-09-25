notas = []
c = 0
soma = 0

while c <= 3 :
    notas.append(float(input("Nota: ")))
    soma = soma + notas[c]
    c +=1
    
print(f"Média {notas} é {soma/4:.1f}")