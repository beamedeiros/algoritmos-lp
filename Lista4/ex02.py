'''Sorteie 20 inteiros entre 1 e 100 numa lista. 
Armazene os números pares na lista
PAR e os números ímpares na lista IMPAR. 
Imprima as três listas.'''

import random

list = random.sample(range(100), 20)
par = [i for i in list if i % 2 == 0]
impar = [i for i in list if i % 2 == 1]

print('Lista: ', list)
print('Par: ', par)
print('Ímpar: ', impar)