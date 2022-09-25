s = 'um tigre, dois tigres, três tigres'

#não altera a variável original
print(s.replace('tigre', 'gato'))
print(s)

#altera a variável original
s = s.replace('tigre', 'gato')
print(s)