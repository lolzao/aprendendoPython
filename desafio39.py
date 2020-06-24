'''
39 - Programa q pergunta ano de nascimento e informa:
1 - se ainda vai se alistar
2 - se é a hora de se alistar
se já passou do tempo do alistamento
O programa deve informar quanto tempo que falta ou que passou do prazo do alistamento
dica: o sistema vai calcular a idade, entao pegar uma forma de fazer esse calculo com o negócio de saber o ano do sistema

'''
from datetime import date
print(date.today().year)
nasc = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
idade = abs(ano - nasc)
maior = abs(18 - idade)
if nasc == 2018:
    print(f'Você está com {idade} anos! Está na hora de se apresentar no serviço militar para se alistar!')
elif idade < 18:
    print(f'Você está com {idade} anos, faltam {18 - idade} anos para se apresentar no serviço militar obrigatório!')
else:
        print(f'Você está com {idade} anos! Você deveria ter se alistado há {maior} anos atrás!')





