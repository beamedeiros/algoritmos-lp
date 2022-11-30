f = open(r'C:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\arquivo\arquivo.txt')

for linha in f.readlines():
    print(linha.strip())
f.close()