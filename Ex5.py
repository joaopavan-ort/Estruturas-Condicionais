'''
5- Crie um programa que peça a idade e classifique: Menor de 13 (Criança), menor de 20 (Adolescente), menor de 60 (Adulto) e 60 ou mais (Idoso).
'''

idade = int(input('Informe sua idade: '))

if idade < 0:
    print('Você não nasceu, idade inválida')
elif idade < 13:
    print('Você é criança.')
elif idade < 20:
    print('Você é adolescente.')
elif idade < 60:
    print('Você é um adulto.')
else:
    print('Você é idoso')
