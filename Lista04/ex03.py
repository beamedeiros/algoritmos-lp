'''Faça um programa que crie
dois vetores com 10 elementos
aleatórios entre 1 e 100. 
Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.
Imprima os três vetores'''

import random

list1 = random.sample(range(100), 10)
list2 = random.sample(range(100), 10)
list3 = []

for i in zip(list1, list2):
    list3.extend(list(i))

print('Lista 1: ', list1)
print('Lista 2: ', list2)
print('Lista 3: ', list3)