'''

Desafios 1 a 3
1 programa que le um número Real e mostre na tela a sua porção inteira, ex: Digite um número: 6.127. O número 6.127 tem a parte Inteira 6

2 programa que le comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
dica: quadrdado da hipotenusa é igual a soma dos quadrados dos catetos
tem modulo pra isso

3 le um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente do angulo
tem modulo pra isso

'''

n = float(input('Digite um número quebrado '))
print(f'O número inteiro de {n} é {int(n)}')

from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)
print(f'Hipotenusa: {hip:.1f}')

import math
ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(ang)
tag = math.tan(ang)
print(f'Seno: {seno}, Cosseno: {cos}. Tangente: {tag}')


