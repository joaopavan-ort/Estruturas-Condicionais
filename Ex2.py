'''
2- Faça um programa que receba uma senha digitada pelo usuário e informe se a mesma é válida ou não (supondo que a senha válida é “ort123”).
'''

senha = input('Insira a Senha: ')

while(True):
    if senha == 'ort123':
        print('Senha correta, bem vindo!')
        break
    else:
        print('Senha incorreta, tente novamente.')
