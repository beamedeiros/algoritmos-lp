def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True

arq = open(r'c:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\IPS\IPS.txt')
validos = open(r'c:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\IPS\Válidos.txt', 'w')
invalidos = open(r'c:\Users\beatriz.santos\Documents\FATEC\algoritmos-lp\Lista6\aulas\IPS\Inválidos.txt', 'w')

for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)

arq.close()
validos.close()
invalidos.close()