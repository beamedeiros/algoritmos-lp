a = 'X'
def func():
    global a
    a = 'O'
func()
print(a)