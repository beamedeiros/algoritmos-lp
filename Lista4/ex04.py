'''Seja o statement sobre diversidade:
“The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”

Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que 
começam ou terminam comuma das letras “python”.
Imprima a lista resultante.
Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas'''

import string

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()

for i in string.punctuation:
    texto = texto.replace(i, ' ')

res = []
for r in texto.split():
    if r[0] in 'python' or r[-1] in 'python':
        res.append(r)

print(res)