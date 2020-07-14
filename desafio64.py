'''
le numeros e para qd ler o 999. No final mostra quantos números foram digitados e a soma entre eles.
'''
n = 0
c = 0
f = 0
while n != 999:
    n = int(input('Digite um número: '))
    c = c + 1
    f = f + n
print('Fim')
print(f'Você digitou {c} números.')
print(f'A soma entre eles é {f-999}')