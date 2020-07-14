'''
53 - le uma frase e diz se eh palíndromo
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
tem a ver com contar de frente pata atrás

'''

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
t = junto[::-1]
print((t))
if junto == t:
    print('é palíndromo!')
else:
    print('Não é palíndromo')