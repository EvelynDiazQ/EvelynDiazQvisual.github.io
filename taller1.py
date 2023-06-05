
numeroIngresado= 0
valor= 0 
i = 0
serie= 0.0
acumulaSerie=0.0  
resultado= 0.0 

numeroIngresado = int(input("Ingrese un valor hasta donde se se debe hallar la sumatoria : "))

while (numeroIngresado<1):
    numeroIngresado= ("Error. Ingrese el valor nuevamente: ")
valor=numeroIngresado
serie= 1/(valor**2) 
while (i<numeroIngresado):
    acumulaSerie= serie + acumulaSerie
    print (str("1/("+ str(valor)+ "^2)"))
    i =i+1
    valor= valor-1 
    if (valor >0 ):
        serie= 1/(valor**2)
resultado= acumulaSerie+ 1 
print("1")
print("El resultado de la sumatoria es: " + str (resultado))





