#vamos hacer una entrada para subirte  auna atracion donde te piden altura y tickets
altura = int(input("Dame tu altura "))
creditos = int(input("Cuantos creditos tienes "))
acompanado = input("Vienes acompañado? (si/no) ")

if creditos < 10:
  print('No tienes los creditos suficientes')
elif altura >= 137:
  print("¡Disfruta del viaje!")
elif altura >= 100 and acompanado.lower() == "si": #esta acompañante hace si pone si se convierte en true de lo contrario es false
  print("¡Disfruta del viaje!")
else:
  print("Todavía no eres lo suficientemente alto para este paseo")