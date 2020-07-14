nome = str(input('Qual seu nome? '))
if nome == 'Rafael': # condição simples
    print(f'{nome}, mas que nome belo!!!')
elif nome == 'Pedro' or nome == 'Nayara' or nome == 'Julia': # com o elif vira estrutura condicional aninhada
    print(f'{nome}, ah, bacana tbm o nome')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print(f'BELEZA, {nome}')
else: # virou condição composta com o if e depois o else. O else é SEMPRE opcional.
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')
