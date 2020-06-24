'''
44 - Calcula valor a ser pago por um produto
pergunta preço normal e condição de pagamento
dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
'''

produto = float(input('Quanto custa o produto? '))
print(f'Seu produto custa R$ {produto:.2f}')
dinheiro = (produto*10)/100
avista = (produto*5)/100
parcela = (produto*20)/100
print('[1] DINHEIRO/CHEQUE:')
print('[2] À VISTA NO CARTÃO:')
print('[3] ATÉ 2X NO CARTÃO:')
print('[4] 3x OU MAIS NO CARTÃO:')
opcao = int(input(f'Selecione a opção de pagamento:'))

if opcao == 1:
    print(f'OPÇÃO 1 10% DE DESCONTO. SAI A R$ {produto - dinheiro:.2f}')
elif opcao == 2:
    print(f'OPÇÃO 2: 5% DE DESCONTO. SAI A R$ {produto - avista:.2f}')
elif opcao == 3:
    print(f'OPÇÃO 3: PREÇO NORMAL. SAI A R$ {produto:.2f}')
elif opcao == 4:
    print(f'OPÇÃO 4: 20% DE JUROS. SAI A R$ {produto + parcela:.2f}')
elif opcao > 4:
    print('Opção inválida!')
