a = 1
while a < 3:
    if a % 2 == 0:
        b = 1
        while b < 3:
            print('X', end = '')
            b += 1
    print('O', end = '')
    a += 1

# faz while dentro do if 