# Programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
msg = input('Digite qualquer coisa ')
print('É alpha: {}, é numérico: {}, é alphanumérico: {}'.format(msg.isalpha(), msg.isnumeric(), msg.isalnum()))
# print(msg.isalpha(), msg.isnumeric(), msg.isalnum(), msg.isascii(), msg.isdecimal(), msg.isdigit(), msg.isidentifier(), msg.islower(), msg.isprintable(), msg.isspace(), msg.istitle(), msg.isupper())
