# Desafio 5: programa que le número inteiro e mostra na tela seu sucessor e antecessor.

# Desafio 6: criar algoritmo que le um número e mostre o dobro, triplo e raiz quadrada.

# Desafio 7:Programa que le duas notas de um aluno e calcula e mostre a média.

# Desafio 8: Programa que le valor em metros e exiba convertido em centímetros e milímetros.
n = int(input('Número?'))
print(f'Antecessor: {n - 1}. Sucessor {n + 1}')
print(f'Dobro: {n * 2} Triplo: {n * 3} Raiz Quadrada: {n ** 0.5:.1f}')
nota1 = int(input('Nota da Primeira Prova: '))
nota2 = int(input('Nota da Segunda Prova: '))
print(f'A média deu: {(nota1 + nota2) / 2}')
tam = float(input('Digite o tamanho em metros: '))
print(f'Tamanho: {tam}m. Em km: {tam / 1000}km. Hectômetro: {tam / 100}hm. Decâmetro: {tam / 10}dam Centímetros: {tam * 100}cm. Decímetro: {tam * 10}dm. Milímetros: {tam * 1000}mm ')
