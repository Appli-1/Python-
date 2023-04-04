import random


numero_secreto = random.randint(0,9)
intentos = 4

#modo bucle para adivinar un numero 
while intentos > 0:
    pregunta = int(input("Adivina el número secreto (entre 1 y 10): "))
    if pregunta == numero_secreto: #adivinas el codgigo 
        print("¡Felicidades! Adivinaste el número secreto.")
        break
    else: #cada vez que intento pase se reduce un numero hasta llegar a 0
        intentos -= 1
        print("Incorrecto. Te quedan", intentos, "intentos.")
#agregamos un if al momneto de llegar intentos a 0 damos el numero secrecto
if intentos == 0:
    print(f"Te quedaste sin intentos el numero era {numero_secreto}")