print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

#usamos el bucle while para cuando cometa el error de pin repita la variable
#hasta que la condicion sea verdadera
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')