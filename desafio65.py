'''
le vários números inteiros.
No final mostra a média entre eles e qual foi o maior e o menor valor lido.
O programa vai perguntar pro usuário se ele quer ou não continuar digitando os valores
'''

lista = []
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print(f'Os números digitados foram: {lista})')
print(f'O maior número digitado foi: {max(lista)}')
print(f'O menor número digitado foi: {min(lista)}')
soma = sum(lista)
media = sum(lista) / len(lista)
print(f'A soma dos números digitados foi: {soma}')
print(f'A média dos números digitados foi: {media}')

