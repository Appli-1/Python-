#vamos hacer una entrada para subirte  auna atracion donde te piden altura y tickets
altura = int(input("Dame tu altura "))
creditos = int(input("Cuantos creditos tienes "))
con_una_persona = bool(input("Vienes acompañado? "))

if creditos < 10:
  print('No tienes los creditos suficientes ')
elif altura >= 137 and creditos >= 10:
  print('Disfruta el viaje!')
elif altura < 137:
  if altura < 100 or not con_una_persona:
    print("Todavía no eres lo suficientemente alto para este paseo")
elif altura >= 100 and  con_una_persona:
  print("¡Disfruta del viaje!")
else:
  print("ERROR")