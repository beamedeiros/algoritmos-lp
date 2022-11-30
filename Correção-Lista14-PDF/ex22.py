repete = True
a = 0
b = 0

while repete:
    print('O', end = '')
    if a + b >= 24:
        repete = False
    a += 5
    b += 7