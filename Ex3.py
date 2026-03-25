'''
3- Faça um programa que leia três notas de um aluno, calcule sua média aritmética e imprima uma mensagem dizendo se o aluno foi 
aprovado, reprovado ou deverá fazer prova final. O critério de aprovação é o seguinte: 
*  aprovado (média ≥ 7); 
*  reprovado (média < 3);
*  prova final ( 3 ≤ média < 7).
'''


while(True):
    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        print('Nota inválida, notas devem ser de 0 a 10')
        n1, n2, n3 = map(float, input('Informe suas 3 notas: ').split())
    else:
        break

m = (n1 + n2 + n3) / 3

if m >= 7:
    print('Sua média foi {:0.1f}. Você foi aprovado!'.format(m))
elif m < 3:
    print('Sua média foi {:0.1f}. Você foi reprovado.'.format(m))
elif 3 <= m and m < 7:
    print('Sua média foi {:0.1f}. Você está de prova final, boa sorte.'.format(m))
