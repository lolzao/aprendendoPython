# 5
frase = str(input('Escreva uma frase ')).strip()
print(frase)
print('Quantidade de As na frase:')
print(frase.count('A')) # Quantos As tem
print('Primeira Posição do A:')
print(frase.find('A')+1) # Primeira posição do A
print('Última posição do A:')
print(frase.rfind('A')+1) # Última posição do A

# 6
nome = str(input('Qual seu nome completo? '))
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e o seu último nome é {nome[-1]}')