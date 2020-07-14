frase = 'Curso em Vídeo Python'
print(frase[3]) # especifiquei da onde começar
print (frase[3:13]) # onde começa e termina
print(frase[:13]) # só onde termina entao começa do 0
print(frase[13:]) # só onde começa então vai até o final
print(frase[1:15])
print(frase[1:15:2]) # pulando de 2 em 2
print(frase[1::2]) # só onde começa pulando de 2 em 2
print(frase[::2]) # toda a string de 2 em 2
print(frase.count('o')) # frase é objeto então quantas vezes aparece a letra o (minúsculo) no frase
print(frase.upper().count('O')) # mandou contar a quantidade de 0 na frase transformada para letra maiúscula
print(len(frase)) # conta o tamanho da frase
print(len(frase.strip())) # strip remove os espaços antes e depois caso a frase tivesse espaço antes e depois
print(frase.replace('Python', 'Android')) # troca a palavra da frase. Obs: a string é imutável, se der um print frase abaixo continua Python:
print(frase)
frase = frase.replace('Python', 'Android') # dessa forma sim consegue alterar a string dentro da frase, criando
print(frase)
frase = 'Curso em Vídeo Python'
print('Curso' in frase) #pergunta se a palavra está dentro da frase
print(frase.find('Curso')) # manda achar a posição da palavra na frase
print(frase.find('video')) #como a palavra não existe o resultado é -1
print(frase.lower().find('vídeo')) # mandei fazer uma procura por vídeo em minúsculo dentro da frase jogada para minúscula
print(frase.split()) # cria uma lista com o separador de espaço a partir da frase
dividido = frase.split()
print(dividido[0]) # manda mostrar o primeiro item da lista
print(dividido[2][3]) # mostra qual a letra 3 dentro do item 2 da lista