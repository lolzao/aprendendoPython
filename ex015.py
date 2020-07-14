# pergunta quantidade de Km percorrido e dias que ele foi alugado. Calcule o preço a pagar. O carro custa 60 reais por dia e 0,15km por Km rodado.
km = float(input('Quantos Kms'))
dia = int(input('Quantos dias'))
price = (km*0.15)+(dia*60)
print(f'Total a pagar: {price:.2f}')