# \033[Style;CorTexto;CorBackm São opcionais
# \033[0;33;44m
# Style: 0(NONE) 1(negrito) 4(sublinha) e 7(inverte as configurações letra e fundo)
# Texto: 30 até 37
# Back: 40 até 47
# fundo branco e letra preta: 7;30
# módulo interessante de cor: colorized

print('\033[31mOlá mundo')
print('\033[31;43mOlá mundo')
print('\033[1;31;43mOlá mundo')
print('\033[1;31;43mOlá mundo\033[m') # tirou as formatações no final para a barra não ir até o final
print('\033[4;30;45mOlá mundo\033[m')
print('\033[30mOlá mundo\033[m')
print('\033[7;30mOlá mundo\033[m') # usou o 7 e inverteu, deixando o fundo branco e a cor da letra preta
print('\033[0;33;44mOlá mundo\033[m')
print('\033[7;33;44mOlá mundo\033[m') # inverteu o de cima
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}') # repara que cancelou a cor pro e não ficar verde.
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m'}
print('testando {}cores{} em {}Python'.format(cores['azul'], cores['limpa'], cores['amarelo']))
