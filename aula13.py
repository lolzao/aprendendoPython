# Estrutura de laço

# estruturas da formatação:

'''

for c in range(1,10):
    passo
pega

'''
# laço com intervalo:

'''
for c in range(0,3):
    passo
    pula
passo
pega

'''

'''
for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega

'''
for c in range(0,6): # O 'c' pode ser o nome que quiser
    print('Oi')
print('FIM')

for c in range(0,6): # Deixou o FIM dentro do laço
    print('Oi')
    print('FIM')

for c in range(0,6):
    print(c)
print('FIM')

for c in range(1,7): #contagem de um até 6 (o ultimo ele ignora)
    print(c)

for c in range(6, 0, -1): #o numero final indica o que quer que ele faça, que nesse caso é contar para atrás, ou sela começa no 6, tira -1 daí vai por 5 e assim sucessivamente.
    print(c)

for c in range(0, 7, 2): #aqui ele vai contar de 0 a 6 de 2 em 2!
    print(c)

n = int(input('Digite um número: '))
for c in range(0, n+1): #botou +1 para ele quando chegar no ultimo número que seria um anterior ao que o usuário digitasse soma +1 para chegar até o numero que o usuario digitou
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo(s): '))
for c in range(i, f, p+1):
    print(c)
print('FIM')

for c in range(0, 3): #vai perguntar 3x o n
    n = int(input('Digite um valor: '))
print('FIM')

print('Vamos somar!!!')
s = 0
for c in range(0, 3): #vai perguntar 3x o n
    n = int(input('Digite um valor: '))
    s = s + n
print(f'O somatório dos numeros da {s}!')



