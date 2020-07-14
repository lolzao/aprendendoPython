n1 = int(input('Digite um valor: '))
print(n1.__class__)
print(type(n1))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre', n1, 'e', n2, 'é', s)

# forma simplificada ensinada no curso:
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# forma atual de fazer format:
print(f'A soma entre {n1} e {n2} vale {s}')
