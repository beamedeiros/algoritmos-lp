def f(x):
    print('x', end = '')
    if x <= 1:
        return 1
    else:
        return x + f(x-1)
