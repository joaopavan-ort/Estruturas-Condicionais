'''
4-  Escreva um programa que vai perguntar ao usuário um número e imprimirá o dia da semana correspondente a esse 
 número (1 = domingo, 2 = segunda, etc), ou dizer se o número digitado é inválido.
'''

dia = int(input('Informe um nº de 1 a 7: '))

if dia == 1:
    print(dia, 'corresponde ao domingo')
elif dia == 2:
    print(dia, 'corresponde à segunda')
elif dia == 3:
    print(dia, 'corresponde à terça')
elif dia == 4:
    print(dia, 'corresponde à quarta')
elif dia == 5:
    print(dia, 'corresponde à quinta')
elif dia == 6:
    print(dia, 'corresponde à sexta')
elif dia == 7:
    print(dia, 'corresponde ao sábado')
else:
    print('Esse número é inválido.')