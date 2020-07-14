# 52 - pergunta numero inteiro e diz se é ou n numero primo
# primo só é divisível por 1 e por ele mesmo, daí o bizu é fazer um for que conte até ele mesmo pra checar se é divisível ou não
n = int(input('Digite um número: '))
tot = 0 # variável criada para saber o número de vezes que ele foi divisível!
for c in range(1, n+1):
    if n % c == 0:
        print(c)
        tot += 1
print(f'O número {n} foi divisível {tot} vezes!')
if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')


