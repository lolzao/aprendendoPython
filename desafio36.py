'''

36- Programa aprova empréstimo para compra de casa
Pergunta:
1 - valor da casa
2 - salário
3 - quantos anos vai pagar
Calcular valor da prestação mensal sabendo que não pode exceder 30% do salário ou então o empréstimo será negado
dica: Pega o valor da casa, divide o valor dos anos que ele colocou e verifica o valor da prestação e por um if prestação > 30% do salário print empréstimo negado
'''

casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário? '))
ano = int(input('Em quantos anos você vai pagar? '))
ano = ano*12
prest = (casa/ano)
cond = (sal*30)/100
if cond < prest:
    print(f'Sua prestação foi de {prest:.2f} e excedeu 30% do seu salário, empréstimo negado')
else:
    print(f'Sua prestação será de {prest:.2f} e seu empréstimo está aprovado!')
