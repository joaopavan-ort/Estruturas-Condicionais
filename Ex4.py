'''
4-  Escreva um programa que vai perguntar ao usuário um número e imprimirá o dia da semana correspondente a esse 
 número (1 = domingo, 2 = segunda, etc), ou dizer se o número digitado é inválido.
'''

dia = int(input('Informe um nº de 1 a 7: '))

while(True):
if dia == 1:
    print(dia, 'corresponde ao domingo')
    break
elif dia == 2:
    print(dia, 'corresponde à segunda')
    break
elif dia == 3:
    print(dia, 'corresponde à terça')
    break
elif dia == 4:
    print(dia, 'corresponde à quarta')
    break
elif dia == 5:
    print(dia, 'corresponde à quinta')
    break
elif dia == 6:
    print(dia, 'corresponde à sexta')
    break
elif dia == 7:
    print(dia, 'corresponde ao sábado')
    break
else:
    print('Esse número é inválido.')
    dia = int(input('Informe um nº de 1 a 7: '))
