#Escribe un programa en python que solicite al usuario su año de nacimiento 
#calculo de la edad
#vericar si es mayor de edad, mensaje

añonacimiento=int(input("Digite su año de nacimiento: "))
añoactual=int(input("Digite el año actual: "))

edad=añonacimiento-añonacimiento
if(edad>18):
    print("Eres mayor de edad")
else:
    print("Eres manor de edad")