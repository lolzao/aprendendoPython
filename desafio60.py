'''
60) pede um número e mostra o seu fatorial. Ex:
5! = 5*4*3*2*1 = 120
'''
valor = int(input('Escolha um valor: '))
c = valor
f = 1
while c > 0:
    print(c, end=' ')
    f = f * c
    c = c - 1
print(f)

