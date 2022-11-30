def fat():
    n = 1
    f = 1
    while True:
        f *= n
        yield f
        n += 1

a = fat()
for i in range(5):
    print(next(a), end = '')