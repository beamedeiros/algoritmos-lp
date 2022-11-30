a = [1, 2, [3, 4]]
print(1 in a, end = '')
print([1, 2] in a, end = '')
print([3, 4] in a, end = '')
print(3 in a, end = '')
print(3 in a[2], end = '')
print(5 not in a)