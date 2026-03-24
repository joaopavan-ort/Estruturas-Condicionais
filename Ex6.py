'''
6- Crie um programa que peça  três lados de um triângulo e diga se 
 ele é Equilátero (3 lados iguais), Isósceles (2 iguais) ou Escaleno (todos diferentes) .
'''

x, y, z = map(float, input('Informe os 3 lados de um triângulo: ').split())

if x == y and y == z:
    print('O triângulo é equilátero.')
elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('O triângulo é isósceles.')
elif x != y and x != z and y != z:
    print('O triângulo é escaleno.')