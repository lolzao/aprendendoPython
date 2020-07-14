'''
51 - primeiro termo e razão de uma PA e no final mostra os 10 primeiros termos dessa progressão.
Eh realizar contagem de um numero ateh o outro pulando de tanto em tanto
ex: contar de 1 até 100 de 10 em 10, isso eh uma PA onde a razão é 10

'''

inicioPA = int(input('Por qual número quer começcar a PA? '))
fimPA = int(input('Qual o número final da PA? '))
razaoPA = int(input('Qual a razão da PA?'))
s = 0
for c in range(inicioPA, fimPA+1, razaoPA):
    print(c)
for c in range(inicioPA, 20, razaoPA):
    print(c)
