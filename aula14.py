# Estrutura de repetição while
'''
Quando sabe o limite, ou seja, quantos passos vou dar, é mais prático usar a estrutura de repetição for. O while é bom quando não sabemos o limite
'''

# estrutura for c in range(1, 10) com print c na segunda linha usando while:

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

# Ou seja, usou mais linhas, o for nesse caso seria mais simples
# Não da para fazer com for um programa que peça um número sem parar e pare de contar um valor quando a pessoa digitar o 0 por exemplo:
n = 1
while n != 0: #nome disso é condição de parada
    n = int(input('Digite um número: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
# ou seja, no while você não precisa determinar um range, pode fazer laços infinitos.

# mostrar quantos números eram pares e quantos ímpares:
n = 1
par = impar = 0
while n != 0: #nome disso é condição de parada
    n = int(input('Digite um número: '))
    if n != 0: #o teste só vai funcionar se o número for diferente de zero, daí a pessoa pode usar o 0 só para cancelar e o zero não entrará na contagem de número par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
