texto = open(r'C:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\texto\texto.txt', 'r')
cripto = open(r'C:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\texto\cripto.txt', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouãõ':
            cripto.write('*')
        else:
            cripto.write(letra)
texto.close()
cripto.close()
