def f(a):
    a += 5
    return a

b = 0
f(b)
print (b, ',', end = '')
b = f(b)
print(b)