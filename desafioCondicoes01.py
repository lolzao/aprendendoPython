'''
28 -
Computador vai pensar em um número inteiro de 0 a 5 e pedir pro usuário tentar descobrir qual o número escolhido e o programa fala se o usuário venceu ou perdeu.
dica: escolher numero aleatório da lista(pensar)
'''

import random
from time import sleep
n = [0, 1, 2, 3, 4, 5]
pc = random.choice(n)
print(f'Pensei no número {pc}')
user = int(input('Escolha um número: '))
print('P R O C E S S A N D O')
sleep(3)
if user == pc:
    print('Você acertou o número')
else:
    print('Você errou!')

# 29 - le a velocidade do carro. Se ultrapassar 80km dizer que foi multado e a multa vai custar 7 reais por cada km acima do limite
vel = int(input('Velocidade do carro: '))
if vel <= 80:
    print(f'Você está indo a {vel}, parabéns e continue respeitando o limite de velocidade!')
else:
    multa = (vel - 80) * 7
    print(f'Sua velocidade é de {vel}, como o limite de velocidade é 80 você será multado em: R$ {multa:.2f}')

# 30 - criar programa que lê número inteiro e mostra se ele é par ou impar dica: tem a ver com resto zero na divisao por 2, if == 0 par else ímpar
n = int(input('Diga o número inteiro: '))
if n % 2 != 0:
    print('Seu número é impar')
else:
    print('Número par')
# 31 - pergunta a distância da viagem em Km. Calcular preço da passagem, cobrando 50 centavos por Km para viagens de até 200km e 45 para viagens mais longas
dist = float(input('Qual a distância da viagem em Km? '))
if dist <= 200:
    print(f'A viagem custará R$ {0.50 * dist:.2f}')
else:
    print(f'A viagem custará R$ {0.45 * dist:.2f}')

# 32 le um ano e diz se é bissexto
from datetime import date # pegar data atual
ano = int(input('Digite o ano para verificar se é bissexto: '))
if ano == 0:
    ano = date.today().year # ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano\033[34m {ano}\033[m é bissexto!')
else:
    print('Não é bissexto')
