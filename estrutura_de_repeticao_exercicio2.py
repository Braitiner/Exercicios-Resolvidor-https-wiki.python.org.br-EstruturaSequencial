# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.
login = str(input('Informe o nome: '))
password = str(input('Informe uma senha: '))
while login == password:
    password = str(input('Senha inválida, informe uma senha diferente do nome: '))
print('Usuário registrado.')
