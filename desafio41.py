'''
41 - pergunta a data de nascimento, calcula a idade e mostra a categoria:
- até 9: Mirim
- até 14: Infantil
- até 19: Junior
- até 20: Sênior
- Acima: MASTER
'''

nasc = int(input('Qual o ano da sua data de nascimento'))
from datetime import date
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print(f'Você tem {idade} anos. Categoria: MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos. Categoria: INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos. Categoria: JUNIOR')
elif idade == 20:
    print(f'Você tem {idade} anos. Categoria: MASTER')
else:
    print(f'Você tem {idade} anos. Categoria: MASTER')
