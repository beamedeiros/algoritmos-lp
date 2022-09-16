x = int(input("Digite um número: "))
k = 1
fat = 1

while k <= x:
    fat *= k
    k += 1

print(f"fat({x}) = {fat}")