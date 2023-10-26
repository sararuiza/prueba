

import os
def suma_numero(): 
    numeros_suma=[]  
    
    while(True):
        try:

            primernumero=int(input("Ingrese un numero: "))
            seguir=input("Desea agregar otro numero SI o NO: ")
            numeros_suma.append(primernumero)
            if (seguir.lower()=="no"):
                break
        except:
            return "ERROR"
    contador=0
    for i in numeros_suma:
        contador=contador + i
    print("La suma de los numeros es igual a: ",contador)



def resta_numero():
    print("resta!!")
    numero_resta=[]

    while(True):
        try:

            segundonumero=int(input("Ingrese el numero que desea restar: "))
            seguirr=input("Desea continuar SI o NO: ")
            numero_resta.append(segundonumero)

            if (seguirr.lower()=="no"):
                break
        except:
            return "ERROR"
    
    contadorr=0
    for i in numero_resta:
        contadorr=abs((i - contadorr))
    print("El resultado de la resta es igual a: ", contadorr)  


def multiplicacion_numero(): 
    numero_multiplicacion=[]

    while(True):
        try: 
            tercernumero=int(input("Ingrese el numero que desea multiplica: "))
            seguirrr=input("Desea continuar SI o NO: ")
            numero_multiplicacion.append(tercernumero)

            if(seguirrr.lowe()=="no"):
                break
        except:
            return "ERROR"

    contadorrr=0
    for i in numero_multiplicacion:

        contadorrr=contadorrr*i
    print("El resultado de la multiplicacion es: ", contadorrr)    



            


def main():
    

    while(True):

        print("Presione para continuar")
        print("***CALCULADORA***")
        print("1. Para sumar")
        print("2. Para restar")
        print("3. Para multiplicar")
        print("4. Para dividir")
        print("5. Para Salir")

        opcion=int(input("Elija una opcion: "))
    
        if(opcion==1):
            os.system("cls")
            suma_numero()
            
        elif(opcion==2):
            os.system("cls")
            resta_numero()

        elif(opcion==3):
            multiplicacion_numero()
        
           


main()

    

