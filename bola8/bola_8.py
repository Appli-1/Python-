import random
preguntame = input("Dime lo que quieras: ")
#una manera para hacer bola8 utilizando una lista y un random.choice para escoger una opcion de la lista 
preguntas = ["Sí definitivamente",  #se crea una lista 
"Es decididamente así",
"Sin duda",
"Respuesta confusa, intenta otra vez",
"Pregunta de nuevo más tarde",
"Mejor no decirte ahora",
"Mis fuentes dicen que no.", "Outlook no tan bueno",
 "Muy dudoso"]


respuestas = random.choice(preguntas) #usar random.choice para una opcion aleatoria de la lista

print(respuestas)

# Magic 8 Ball 🎱
# otra forma utilizando el if, elif, else

import random

pregunta = input()

random_number = random.randint(1, 9)#generamos un numero random del 1 al 9

if random_number == 1:             #generamos un if, elif para que seleciona la opcion del numero que salgo
  respuesta = 'Yes - definitely'
elif random_number == 2:
  respuesta = 'It is decidedly so'
elif random_number == 3:
  respuesta = 'Without a doubt'
elif random_number == 4:
  respuesta = 'Reply hazy, try again'
elif random_number == 5:
 respuesta = 'Ask again later'
elif random_number == 6:
 respuesta = 'Better not tell you now'
elif random_number == 7:
  respuesta = 'My sources say no'
elif random_number == 8:
  respuesta = 'Outlook not so good'
elif random_number == 9:
  respuesta = 'Very doubtful'
else:
  respuesta = 'Error'
  
print('Pregunta:      ' + pregunta) 
print('Magic 8 Ball:  ' + respuesta)