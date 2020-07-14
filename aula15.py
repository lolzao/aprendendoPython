# condição de parada com break:

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale {s}')
# formatações:

nome = 'José'
print(f'{nome:20} é legal') #nome com 20 espaços
print(f'{nome:^20} é legal') #nome centralizado
print(f'{nome:-^20} é legal') #traço antes e depois
print(f'{nome:->20} é legal') #alinhado à direita
