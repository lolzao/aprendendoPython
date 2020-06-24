'''
40 - programa que le 2 notas de um aluno, calcula a média, mostrando uma mensagem no final, de acordo com a média:
- média abaixo de 5.0, reprovado
- média entre 5.0 e 6.9, recuperação
- média 7.0 ou superior, aprovado

'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é {media:.1f}')
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <=6.9:
        print('Recuperação')
else:
      print('Aprovado')
