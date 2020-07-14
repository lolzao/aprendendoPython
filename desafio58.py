'''
58) melhorar o jogo do desafio 28 (advinhar número), porém o jogador vai ter que tentar até acertar e no final mostra quantos palpites foram necessários para vencer.

'''

import random
from time import sleep
n = [0, 1, 2, 3, 4, 5]
pc = random.choice(n)
palpite = 0
user = int(input('Escolha um número: '))
print('P R O C E S S A N D O')
sleep(1)
if user == pc:
    print('Você acertou o número de primeira!')
while user != pc:
    user = int(input('Você errou. Tente novamente: '))
    palpite += 1
    if user == pc:
        print(f'Você acertou! Foram necessárias {palpite+1} tentativa(s)')
