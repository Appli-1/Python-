
#hacer que el y el 5 iguales en multiplos publique Fizzbuzz
#hacer que los multiplos de 3 sean = a Fizz
#hacer que los multiplos de 5 sean = a Buzz 
#toodo en un rango de 1 al 100

for multi in range(1, 101):
    if multi % 3 == 0 and multi % 5 == 0:
     print("FizzBuzz " +str(multi))
    elif multi % 5 == 0:
        print("Buzz " +str(multi))
    elif  multi % 3 == 0:
        print("Fizz " +str(multi))
else:
    print(multi)
    
    