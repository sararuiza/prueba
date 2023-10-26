# #simular el lanzamiento de un dado de 6 caras
# #saldo inicial 100, puede apostar
import random

import os


def main():

    resultadopersona=[]
    resultadooponente=[]

    input("Presione enter para continuar")
    print("Bienvenido usuario")
    print("en este juego usted lanzara 3 veces seguidas un dado")
    print("si la suma total de sus intentos es mayor que la del oponente")
    print("usted ganara")
    print("ES SU TURNO")


    dado=[1,2,3,4,5,6]
    intento = 0
    while intento < 3 :
    
        opcion=input("Para su lanzamiento escriba ok: ")

        if(opcion.lower()=="ok"):

            aleatorio=random.choice(dado)

            resultadopersona.append(aleatorio)
            print("Su resultado es igual a: ", aleatorio) 
        intento += 1

    print("el resultado total de su intento fue: ", sum(resultadopersona))

    print("ES EL TURNO DEL OPONENTE")
    input("Presione enter para continuar")

    intento2=0
    
    while intento2<3:

      
        
        aleatorio2=random.choice(dado)
        resultadooponente.append(aleatorio2)
        print("El resultado del oponente es igual a: ", aleatorio2)
        intento2+=1

    print("El resultado total del oponente fue:  ",  sum(resultadooponente))



    if sum(resultadooponente)> sum(resultadopersona):
        print("Oponente ganador")

    elif sum(resultadooponente)== sum(resultadopersona):
        print("Empate")
    else:
        print("Usuario es el ganador")




main()

