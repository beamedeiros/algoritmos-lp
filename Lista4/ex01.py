'''Sorteie 10 inteiros entre 1 e 100 para uma lista
e descubra o maior e o menor valor, sem usar
as funções max e min.'''

import random

list = random.sample(range(100), 10)
max = min = list[0]

for i in list[1:]:
    if i > max:
        max = i
    
    if i < min:
        min = i

print('Lista:', list)
print('Maior: ', max)
print('Menor: ', min)