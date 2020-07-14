'''
56 - desenvolva programa que le nome, idade e sexo de 4 pessoas e no final mostre:
média de idade do grupo
qual nome do homem mais velho
quantas mulheres tëm menos de 20 anos
'''

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------- {p} PESSOA -------')
    nome = str(input('Nome? '))
    idade = int(input('Idade? '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: # COM ISSO a idade vai ficar mudando conforme as outras pessoas coloquem número maior.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres menores de 20')



