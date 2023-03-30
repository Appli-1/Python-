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
elif respuesta == "a" and respuesta1 == "b" and respuesta2  == "b":
    print("Bienvenido a Hufflepuff")
elif respuesta == "b" and respuesta1 == "c" and respuesta2  == "c":
    print("Bienvenido a Ravenclaw")
elif respuesta == "b" and respuesta1 == "a" and respuesta2  == "a":
    print("Bienvenido a  Hufflepuff")
elif respuesta == "b" and respuesta1 == "b" and respuesta2 == "b":
    print("Bienvenido a Slytherin")
else:
     print("Error")
