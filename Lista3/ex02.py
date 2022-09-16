# Faça um programa que leia um nome de
# usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usu = str(input("Digite um nome de usuário: "))
senha = str(input("Digite uma senha diferente do usuário: "))

while usu == senha:
    print("Senha inválida!")
    usu = str(input("Digite um nome de usuário: "))
    senha = str(input("Digite uma senha diferente do usuário: "))