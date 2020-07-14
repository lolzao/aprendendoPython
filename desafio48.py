'''
48 - calcula a soma entre todos os numeros ímpares que sao multiplos de 3 e se encontram no intervalo de 1 até 500

'''

cont = 0 # o contador vai contar +1
s = 0 # o acumulador vai acumulando os valores que eu determinar.
for c in range(0,501):
    if c % 2 != 0 and c % 3 == 0:
        s = s+c
        cont = cont + 1
print(f'O somatório dos numeros ímpares multiplos de 3 no intervalo de 1 até 500 deu {s} e a quantidade de números foi {cont}')
















