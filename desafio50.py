'''
50 - pergunta 6 numeros inteiros e mostra a soma apenas dos que forem pares. Se o valor digitado for ímpar desconsiderar
'''

s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print(s)
