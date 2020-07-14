'''

Desafio 4 a 6

4 Sorteio de 4 alunos para apagar o quadro
programa vai ler o nome dos alunos e dizer o escolhido


5 Professor quer sortear a ordem de apresentação de trabalho dos alunos. Tem que ler o nome dos 4 alunos e mostrar a ordem sorteada.

6 Programa que abre e reproduz o audio de um MP3


'''

import random
a1 = 'Maria'
a2 = 'João'
a3 = 'José'
a4 = 'Pedrinho'
sorteio = random.choice([a1, a2, a3, a4])
print(f'Atenção {a1}, {a2}, {a3} e {a4}! Quem vai apagar o quadro hoje é você {sorteio}!')

ordem = [a1, a2, a3, a4]
random.shuffle(ordem)
print(f'Atenção {a1}, {a2}, {a3} e {a4}!')
print(f'Ordem de apresentação do trabalho: \n {ordem} ')
