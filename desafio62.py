inicioPA = int(input('Por qual número quer começar a PA? '))
razãoPA = int(input('Qual a razão da PA? '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{inicioPA}', end=' ')
        inicioPA = inicioPA + razãoPA
        c = c + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(f'O programa encerrou e foram {total} termos mostrados')
