anio= 0 

divisibleX4=0
divisibleX100=0
divisibleX400=0
anio=int(input("Ingrese el año: ")) #anio = 1900

divisibleX4=anio%4
divisibleX100=anio%100
divisibleX400=anio%400

if ((divisibleX4==0 and divisibleX400 == 0) or (divisibleX100 == 0)):
#esBisiesto=bool(1)
  print ("Año " + str(anio)+" es bisiesto")
else:
 print ("Año " + str(anio)+" no es bisiesto")


 #if (esBiesto):
 # print ("Año " + str(anio)+" es bisiesto")
 #else:
 # print ("Año " + str(anio)+" no es bisiesto")