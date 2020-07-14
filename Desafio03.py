# Desafio 11: Programa que le a largura e altura de uma parede em metros e calcula a área e a quantidade de tinta necessária pra pintar, cada litro de tinta pinta uma área de 2m2.

# Desafio 12: algoritmo que le o preço de um produto e mostra seu novo preço com 5% de desconto.

# Desafio 13: mostra o salário de um funcionário e seu novo salário com 15% de aumento.

larg = float(input('Largura: '))
alt = float(input('Altura: '))
area = larg * alt
print(f'A parede tem {area}m2')
print(f'Será necessário {area/2} litros de tinta para pintar a parede')

price = float(input('Preço do Produto: '))
desc = (price*5)/100
final = price-desc
print(f'O produto custa {price}. Com o desconto de 5% fica {final:.2f}')

sal = float(input('Salário do Funcionário: '))
aum = (sal*15)/100
print(f'O funcionário recebe atualmente {sal:.3f}, com o aumento de 15% receberá {sal+aum:.3f}')
