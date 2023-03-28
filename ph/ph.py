ph = float(input("introduce tu ph "))#saber el ph de una persona metodo float para saber valores flotantes


#usamos elif para tener mas opciones si una no es 
if ph > 7:
    print("Tu ph es basico")
elif ph < 7:
    print("Tu ph es acido")
else:
    print("tu ph es neutral")