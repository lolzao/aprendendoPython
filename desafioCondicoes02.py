# 33 - programa que lê 3 números e mostra qual é o maior e qual o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = [n1, n2, n3]
lista = sorted(lista)
print(lista)
print(f'{lista[0]} é o menor número e {lista[2]} é o maior número')

sal = float(input('Qual seu salário? '))
aum1 = (sal*10)/100
aum2 = (sal*15)/100
if sal > 1250:
    print(f'Seu salário ganhará aumento de 10%, logo ficará: {sal+aum1:.2f}')
else:
    print(f'Seu salário ganhará aumento de 15%, logo ficará: {sal+aum2:.2f}')

# 35 - comprimento de 3 retas e diz se pode ou ñ formar um triângulo pesquisar princípio matemático para saber quais retaspodem  formar um triângulo
# cada seguimento tem que ser menor do que a soma do cumprimento dos outros dois
r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É triângulo')
else:
    print('Não é triângulo')
