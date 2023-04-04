#codigo para saber que tipo de casa eres em harry potter 
print('--------------')
print("Te gusta el Amanecer o Crepusculo?")
print("a) Amanecer")
print("b) Crepusculo")
print('--------------')
respuesta = input("Dame la opcion que piensas")

print('--------------')
print("Cuando este muerto, quiero que la gente me recuerde como: ")
print("a) El bueno")
print("b) El mejor")
print("c) El sabio")
print("d) El audaz")
print('--------------')
respuesta1 = input("Dame la opcion que pienses que eres ")

print('--------------')
print("¿Qué tipo de instrumento agrada más a tu oído? ")
print("a) El violin")
print("b) La trompeta")
print("c) El piano")
print("d) El tambor")
print('--------------')
respuesta2 = input("Dame la opcion  ")

if respuesta == "a" and  respuesta1 == "d" and respuesta2 == "d":
    print("Bienvenido a Gryffindor")
elif respuesta == "a" and respuesta1 == "c" and respuesta2  == "c":
    print("Bienvenido a Ravenclaw")
elif respuesta == "a" and respuesta1 == "a" and respuesta2  == "a":
    print("Bienvenido a Slytherin")
elif respuesta == "a" and respuesta1 == "b" and respuesta2  == "b":
    print("Bienvenido a Hufflepuff")
elif respuesta == "b" and respuesta1 == "c" and respuesta2  == "c":
    print("Bienvenido a Ravenclaw")
elif respuesta == "b" and respuesta1 == "a" and respuesta2  == "a":
    print("Bienvenido a  Hufflepuff")
elif respuesta == "b" and respuesta1 == "b" and respuesta2 == "b":
    print("Bienvenido a Slytherin")
elif respuesta == "b" and respuesta1 == "d" and respuesta2 == "d":
    print("Bienvenido a Gryffindor")
else:
     print("Error")



#otra forma de implemetarlo dandole varibales y su valor al final
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

#hacemos un if para ver quien es maypr de tal o igual 
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')