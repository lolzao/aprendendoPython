'''
59) programa que pede dois valores e mostra um menu na tela:
[1] somar
2 multiplicar
3 maior
4 novos números
5 sair do programa
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = 0
while menu != 5:
    menu = int(input(
    '''
    O que deseja fazer?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] Digitar outros valores
    [5] SAIR
    '''))
    if menu == 1:
        print(n1 + n2)
    if menu == 2:
        print(n1*n2)
    if menu == 3:
        if n1 < n2:
            print(f'{n2} é maior')
        else:
            print(f'{n1} é maior')
    if menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    if menu == 5:
        print('Fim')
    else:
        print('Número inválido, tente novamente!')