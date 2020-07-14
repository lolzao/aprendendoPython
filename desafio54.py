# 54 - pergunta ano de nascimento de 7 pessoas (logo 7x) e mostra quantas ainda não atingiram a maioridade e quantas ja sao maiores

from datetime import date
ano = date.today().year
s = 0
u = 0
for c in range(1, 8):
    nasc = int(input(f'Qual o ano de nascimento da {c}º pessoa? '))
    idade = ano - nasc
    if idade >= 18:
        print('Maior de idade')
        s = s + 1
    elif idade < 18:
        print('Menor de idade!')
        u = u + 1
print(f'{s} pessoas são maiores de idade e {u} pessoas são menores de idade')
