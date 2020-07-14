nome = str(input('Nome Completo? ')).strip()
print(nome)
print(f'seu nome em minúsculo é {nome.lower()}')
separar = nome.split()
nome = ''.join(separar)
print (nome)
print(f'Sem considerar o espaço seu nome tem {len(nome)} letras')
print (separar[0])
primeiro = separar[0]
print(f'seu primeiro nome tem {len(primeiro)} letras')

# 2 criar outro py para fazer matematicamente o exercício
n = int(input('Digite um número de 0 a 9999 '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print (f'unidade: {u}')
print (f'dezena: {d}')
print (f'centena: {c}')
print (f'milhar: {m}')

# 3 forma simples: print(cidade[:5] == 'Santo'
cidade = str(input('Qual nome da sua cidade? ')).strip()
print('Sua cidade começa com o nome Santo? True se tiver e False se não: ')
cidade = cidade.upper().split()
print('SANTO' in cidade[0])

# 4
nome = str(input('Qual seu nome ')).strip()
print('Digite seu nome completo, informaremos se seu nome tem Silva indicando True ou False')
print('silva' in nome.lower())
