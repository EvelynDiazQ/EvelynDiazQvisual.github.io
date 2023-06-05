# Crear un progama en python que muestre los primeros 12 números de la sucesión de
# Fibonacci. La sucesión comienza con
# los números 0 y 1 y, a partir de éstos debe
# imprimirse la secuencia. 
# La salida del programa debe ser: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55 - 89

semilla0 = 0
semilla1 = 1
fibonacci = 0
i = 0
limite = 12

print("Imprimiendo secuencia...")
while (i < limite):
   if(i == 0):
      print (semilla0, end=',')
   if(i == 1):
      print (semilla1, end=',')
   if(i > 1):
        fibonacci = semilla1 + semilla0 
        semilla0 = semilla1
        semilla1 = fibonacci 
        print(fibonacci, end=',')
   i = i + 1
    



