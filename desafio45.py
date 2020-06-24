'''
45 - Jokenpô
criar lista com Pedra, Papel e Tesoura para randomizar a escolha do computador
'''

import random
lista = ['Pedra', 'Papel', 'Tesoura']
print(' [1] Pedra \n [2] Papel \n [3] Tesoura')
escolha = random.choice(lista)
jogador = int(input('Escolha sua arma: '))

if jogador == 1 and escolha == 'Pedra':
    print(f'Os dois escolheram {escolha}. Empate')
elif jogador == 1 and escolha == 'Papel':
    print(f'{escolha} ganha de Pedra! Você perdeu!') # Pedra X Papel = Papel
elif jogador == 1 and escolha == 'Tesoura':
    print(f'{escolha} perde de Pedra. Você ganhou!') # Pedra X Tesoura = Pedra
elif jogador == 2 and escolha == 'Pedra':
    print(f'{escolha} perde de Papel! Você ganhou!') # Papel X Pedra = Papel
elif jogador == 2 and escolha == 'Papel':
    print(f'Os dois escolheram {escolha}. Empate')
elif jogador == 2 and escolha == 'Tesoura':
    print(f'{escolha} ganha de Papel. Você perdeu!') # pAPEL X Tesoura = Tesoura
elif jogador == 3 and escolha == 'Pedra':
    print(f'{escolha} ganha de Tesoura. Você perdeu!') # Tesoura X Pedra = Pedra
elif jogador == 3 and escolha == 'Papel':
    print(f'{escolha} perde de Tesoura. Você ganhou!') # Tesoura X Papel = Tesoura
elif jogador == 3 and escolha == 'Tesoura':
    print(f'Os dois escolheram {escolha}. Empate')
