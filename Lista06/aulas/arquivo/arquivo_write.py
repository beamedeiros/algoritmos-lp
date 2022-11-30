f = open(r'C:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\arquivo\arquivo.txt', 'w')

for linha in range(1,101):
    f.write(f'{linha}\n')
f.close()