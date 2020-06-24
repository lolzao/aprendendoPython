'''

43 - pergunta peso e altura
calcula IMC e mostra:
Abaixo 18.5: abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40 Obesidade
Acima de 40: Obesidade mórbida

'''

peso = float(input('Peso? '))
alt = float(input('Altura: '))
imc = peso / (alt**2)
print(f'IMC: {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
