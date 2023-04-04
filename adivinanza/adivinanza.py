import random


numero_secreto = random.randint(0,9)
intentos = 4

#modo bucle para adivinar un numero 
while intentos > 0:
    pregunta = int(input("Adivina el número secreto (entre 1 y 10): "))
    if pregunta == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break
    else:
        intentos -= 1
        print("Incorrecto. Te quedan", intentos, "intentos.")

if intentos == 0:
    print(f"Te quedaste sin intentos el numero era {numero_secreto}")