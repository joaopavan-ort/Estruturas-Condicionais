'''
6- Crie um programa que peça  três lados de um triângulo e diga se 
 ele é Equilátero (3 lados iguais), Isósceles (2 iguais) ou Escaleno (todos diferentes) .
'''

x, y, z = map(float, input('Informe os 3 lados de um triângulo: ').split())

if x == y and y == z:
    print('O triângulo é equilátero.')
elif x == y or x == z or y == z:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
