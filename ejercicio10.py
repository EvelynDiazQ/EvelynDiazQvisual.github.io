#Ejercicio11. Realizar un programa en Python en el que el usuario ingrese un número entero y
#devuelva como resultado si el número es perfecto o no.
#numeroperfecto: es un número entero positivo que es igual a la suma de sus divisores propios positivos.

numero=int(input("Ingrese un número entero : "))
def numeroPerfecto(numero):
    suma=0 
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i 
    return suma== numero
print( numeroPerfecto(numero))  
   