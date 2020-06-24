'''
42 - Refazer o desafio dos triângulos acrescentando recurso para mostrar o tipo do triângulo que será formado:
- Equilátero: todos lados iguais
- Isósceles: 2 lados iguais
- Escaleno: todos lados diferentes
dica: a correcao desse desafio vai mostrar maneiras diferentes de aninhar condicoes

'''

r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É triângulo')
if r1 == r2 and r2 == r3 and r3 == r1:
    print('Lados iguais, triângulo Equilátero')
if r1 == r2 or r1 == r3 or r2 == r3:
    print('2 lados iguais, Isósceles')
if r1 != r2 or r1 != r3 or r2 != r3:
    print('Todos os lados diferentes: Escalenos')
else:
    print('Não é triângulo')
