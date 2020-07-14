# 55 - le o peso de 5 pessoas (ou seja 5x no for) e no final mostra qual foi o maior e o menor peso lidos.

peso = []
for c in range(1, 6):
    peso.append(float(input(f'Qual o peso da {c}º pessoa? ')))
print(f'O menor peso é {min(peso)} e o maior é {max(peso)}')
