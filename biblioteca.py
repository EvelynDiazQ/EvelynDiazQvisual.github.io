#Name: biblioteca.py
# biblioteca en donde se agrupapn funciones que se utilizan comunmente para importarlas 
# desde otro programa python

import math as ma 


########################################################################################
#Función esNum, recibe un parámetro 
#verifica si el parámetro es un numero entero. 
# va a retornar true si es numero false en caso que no lo sea
#
###########################################################################################

def esNum(a) :
    try:
        int(a)
    except:
        return False
    return True

############################################################################################
#     funcion factorial, recibe un parametro,
#  devuelve el factorial de un numero
#############################################################################################

def funcionFactorial(numero):
    factorial=1
    if (numero< 0 ):
        factorial=0 
    elif (numero==0 ):
        facotrial=1
    else:
        while (i<=numero):
            factorial= factorial *i 
            i=i+1
    return factorial 

# ###########################################################################################
# funcion quitarEspBlanCadena, recibe un parámetro 
# devolver la cadena sin espacios en blanco
#############################################################################################

def quitarEspBlacCadena(cad):
    i=0 
    longitud= len(cad)
    cadResultado =""

    while (i<longitud):
        if (cad[i] !=" "):
            cadResultaso= cadResultado + cad [i]
            i= i + 1
            return cadResultado 

#############################################################################################
# funcion invertirCadena, recibe un parámetro, 
#  devolver la cadena invertida
#############################################################################################

def invertirCadena (cad):
    cadInvertida=""
    i= len(cad)-1

    while (i>= 0):
        cadInvertida= cadInvertida + cad[i]

        i=i-1
    return cadInvertida

###########################################################################################
#funcion esPalindrome, recibe un parámetro, 
#retorna true si la cadena es palindrome  caso contrario falso 
###########################################################################################
def esPalindrome(cadena1):
    palindrome= False
    cadSinEsp= ""
    cadInvertida=""

    cadSinEsp= quitarEspBlacCadena(cadena1.lower())
    cadInvertida= invertirCadena(cadSinEsp)
    if (cadSinEsp== cadInvertida):
        palindrome=True

    return palindrome 

#########################################################################################
# suma 
#########################################################################################

def sumar(num1,num2):
     return num1+num2

########################################################################################
# resta
########################################################################################

def restar(num1,num2):
    return num1-num2

########################################################################################
# multiplicar
########################################################################################    

def multiplicar (num1, num2):
    return num1*num2

########################################################################################
# dividir
########################################################################################

def dividir (num1,num2):
    resultado=0
    if (num2==0):
        print=("Error ...No existe división por cero")
    else:
        resultado= num1/num2

    return  resultado

#######################################################################################
#potencia
#######################################################################################

def potencia(base,exponente):


    return ma.pow (base, exponente)

######################################################################################
#funcion raiz cuadrada, recibe un parametro, 
##
######################################################################################

def raiz(base):
    resultado=0 
    if (base < 0):
        print ("Error ....No es posible calcular la raiz de un numero negativo")
    else:
        resultado= ma. sqrt(base)

    return resultado
