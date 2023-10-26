#ingresar peso en kg
#ingresar altura en metros
#calcular IMC

def main():

    while(True):

        input("Para continuar oprima enter")
        print("**CALCULO DE IMC**")
        peso=float(input("Ingrese su peso en kilogramos: "))
        altura=float(input("Ingrese su estatura en metros: "))

        icm=round((peso/(altura*altura)),2)
        print("Su ICM es igual a: ",icm)

        if(icm<18.5):
            print("Usted esta por debajo de su peso ideal")
        
        elif (icm>18.5 and icm<24.9):
            print("Usted esta en el rango saludable")

        elif (icm>25 and icm<29.9):
            print("Usted tiene sobrepeso")

        elif (icm>30 and icm<34.9):
            print("Usted tiene obesidad grado I")
    
        elif (icm>35 and icm<39.9):
            print("Usted tiene obesidad grado II")

        else:
            print("Usted tiene obesidad grado III")
        



main()

        