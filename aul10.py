# Condições

nome = str(input('Qual é seu nome? '))
if nome == 'Rafael': # estrutura simples só tem o if
    print('Que nome bonito você tem!')
else: # com o else vira estrutura composta
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'Sua média foi {m:.1f}')
print('PARABÉNS' if m>= 6 else 'ESTUDE MAIS') # condição simplificada, fica mais confuso imo
