'''
1- Faça um programa que leia 2 números e imprima uma mensagem dizendo o maior deles.
 Detalhe: se os números forem iguais, imprima uma mensagem avisando ao usuário.
'''

x, y = map(float, input('Informe o valor de dois números, X e Y: ').split())

if x > y:
    print(x, 'é o maior')
elif x < y:
    print(y, 'é o maior')
else:
    print('{} é igual a {}, nenhum é maior que o outro'.format(x, y))
