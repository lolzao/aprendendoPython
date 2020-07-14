'''
57) pergunta sexo de uma pessoa e só aceite os valores M ou F. Caso esteja errado pede para digitar de novo até o valor estar correto
'''

sexo = str(input('Qual seu sexo? ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Digite novamente: ')).upper().strip()[0]
