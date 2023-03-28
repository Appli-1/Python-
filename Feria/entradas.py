#vamos hacer una entrada para subirte  auna atracion donde te piden altura y tickets
altura = int(input("Dame tu altura "))
creditos = int(input("Cuantos creditos tienes "))


if altura >= 137 and creditos >= 10:
  print('Disfruta del viaje ')

if altura < 137 and creditos >= 10:
  print('No tienes la altura suficiente ')
elif creditos < 10:
    print("no tienes los creditos suficicientes")
else:
    print("ERROR")