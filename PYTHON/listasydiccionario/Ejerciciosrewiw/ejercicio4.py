#ingresar su nombre
#retornar un saludo personalizado, segun la hora del dia

import datetime


def main():

    while(True):


        input("Presione para continuar: ")

        print("Bienvenido usuario")
        nombre=input("¿Cual es tu nombre?: ")
        
       
        fecha=datetime.datetime.now()
        hora=datetime.datetime.strftime(fecha, "%H")
        

        if(hora>"1" and hora<"12"):
            print("Buenas dias ", nombre, ",", "ten linda mañana")

        if(hora>"12" and hora<"18"):
            print("Buenas tardes ", nombre,"," "ten linda tarde")

        if(hora>"18" and hora<"24"):
            print("Buenas noches ", nombre,"," "ten linda noche")
        

main()



