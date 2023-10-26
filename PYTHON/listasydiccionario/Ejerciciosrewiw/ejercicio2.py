#ingresar una cantidad en moneda extranjera
#ingresar tasa de cambio
#convertir a otra moneda
#mostrar a cuanto equivale la moneda

while(True):

    print("************************")
    print("***Bienvenido usuario***")
    print("************************")
    print("1.Convertir de peso colombiano a dolares")
    print("2.Convertir peso colombiano a euros")
    print("3.Convertir peso colombiano a pesos mexicano")


    opcion=int(input("Ingrese una opcion: "))

    if(opcion==1):
        moneda=int(input("Ingrese el valor de la moneda actual: "))
        tasa=int(input("Ingrese la tasa actual del dolar: "))
        dolar=moneda/tasa
        c=round(dolar,2)

        print("El valor en dolares es igual a: ", c)

    elif(opcion==2):
        moneda=int(input("Ingrese el valor de la moneda actual: "))
        tasa=int(input("Ingrese la tasa actual del dolar: "))
        euro=moneda/tasa
        c=round(euro,2)

        print("El valor en dolares es igual a: ", c)

    elif(opcion==3):
        moneda=int(input("Ingrese el valor de la moneda actual: "))
        tasa=int(input("Ingrese la tasa actual del dolar: "))
        pesomexicano=moneda/tasa
        c=round(pesomexicano,2)

        print("El valor en dolares es igual a: ", c)


    else:
        print("Valor ingresado no dispnible")
        break




