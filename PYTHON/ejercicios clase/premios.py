#MODULO MANTENIMIENTO DE CODERS
#Sara Camila Ruiz Arismendi-1039421889-grupo 1A

import os

def ingresa_datos(grupo_codersa):

    try:
        nombre=input("Ingrese el nombre y apellido el coder: ")
        edad=int(input("Ingrese la edad del couder: "))
        grupo=input("Ingrese el grupo de coder a, b, o c: ")
        mes_ingreso=int(input("Ingrese el numero del mes de ingreso del couder: "))
        monitor=int(input("Ingrese el numero de monitorias de clase"))
        inasistencias=int(input("Ingrese el numero de inasistencias de clase"))
        talleres=int(input("Ingrese el numero de talleres realizados aprobados en 5 en clase"))
        test=int(input("Ingrese el numero de test aprovados en 5 de clase"))
        participacion=int(input("Ingrese el numero de participaciones en clase"))

        ingreso={"nombre": nombre, "edad": edad, "grupo": grupo , "mes_ingreso": mes_ingreso, "monitor": monitor, "inasistencias": inasistencias, "talleres": talleres, "test": test, "participacion": participacion}

        grupo_codersa.append(ingreso)

        print("Coder agregado al grupo A exitosamnete")

    except:
        print("Los valores ingresados no son validos")



def buscar_coders(grupo_codersa):
    mostrar_grupo(grupo_codersa)


    if not (grupo_codersa):
        print("No se encuentra nadie registrado en este grupo")
    else: 

        buscar=input("Ingrese el nombre y apellido del coder que desea buscar: ")




        for index, valor in enumerate((grupo_codersa)):
            if(valor["nombre"].lower()==buscar.lower()):
                print("El coder: ", valor["nombre"], "esta en el grupo", valor["grupo"])




def eliminar_coders(grupo_codersa):
    mostrar_grupo(grupo_codersa)  

    try:

        eliminar=int(input("Ingrese el indice del coder que va a eliminar: "))


        grupo_codersa.pop(eliminar)

        print("Coder eliminado exitosamente\n")
        print("Tu lista actualizada coders es: ")
        mostrar_grupo(grupo_codersa)   


    except:
        print("Los valores ingresados no son validos")



def mostrar_grupo(grupo_codersa):
    if not grupo_codersa:
         print("No hay coder agregados previamiente")

    else:
        print("CODERS GRUPO A")

        for index, valor in enumerate(grupo_codersa):
            print(index, valor["nombre"], "-",valor["edad"], "-",valor["grupo"],"-", valor["mes_ingreso"])



def actualizar_coders(grupo_codersa):
    mostrar_grupo(grupo_codersa)

    if not grupo_codersa:
        print("El grupo esta vacio, intente nuevamnete")      

    else:

        try:

            indice=int(input("Ingrese el indice del coder a actualizar: "))

            if(indice<0 or indice >len(grupo_codersa)):
                print("El indice ingresado no corresponde a ningun coder")

            else:

                nombre=input("Ingrese el nuevo nombre y apellido del coder: ")
                edad=int(input("Ingrese la nueva edad del coder: "))
                grupo=input("Ingrese el nuevo grupo del coder: ")
                mes_ingreso=int(input("Ingrese el nuevo mes de ingreso del coder: "))

                grupo_codersa[indice]["nombre"]=nombre
                grupo_codersa[indice]["edad"]=edad
                grupo_codersa[indice]["grupo"]=grupo
                grupo_codersa[indice]["mes_ingreso"]=mes_ingreso

        except:
            print("El valor ingresado debe ser un numero")



def premiacion(grupo_codersa,grupo_codersb,grupo_codersc):

    maximo_participacion=0

    for index, valor in enumerate(grupo_codersa):


        if valor["participacion"]>maximo_participacion:

            maximo=valor["participacion"]

    print(maximo_participacion)









def main():

    grupo_codersa=[{"nombre": "jorge hoyos", "edad": int(28), "grupo": "a", "mes_ingreso": int(2), "monitor": int(0), "inasistencias": int(0), "talleres": int(4),"test": int(5), "participacion": int(10)},
                   {"nombre": "sandra velez", "edad": int(17), "grupo": "a", "mes_ingreso": int(2), "monitor": int(4), "inasistencias": int(1), "talleres": int(5),"test": int(5), "participacion": int(20)},
                   {"nombre": "david ruiz", "edad": int(25), "grupo": "a", "mes_ingreso": int(2), "monitor": int(0), "inasistencias": int(0), "talleres": int(2),"test": int(4), "participacion": int(25)}]
    grupo_codersb=[]
    grupo_codersc=[]


    while(True):
        print("Señor trainer")
        print("Bienvenido al modulo de coders")
        input("Presione enter para continuar")
        print("*****************")
        print("***BIENVENIDOS***")
        print("*****************")
        print("1.Para grupo A ")
        print("2.Para grupo B ")
        print("3.Para grupo C ")
        print("4.Para premiacion")
        print("5.Para salir")

        opcion_grupo=int(input(" Seleccione una opcion para continuar: "))
        if(opcion_grupo==1):


            print("1.Para ingresar datos del coder")
            print("2.Buscar couders")
            print("3.Para eliminar Coders")
            print("4.Mostrar los grupos de coders")
            print("5.Para actualizar datos de couders")


            opcion1=int(input("Seleccione una opcion para continuar: "))

            if(opcion1==1):
                os.system("clear")
                ingresa_datos(grupo_codersa)

            if(opcion1==2):
                os.system=("clear")
                buscar_coders(grupo_codersa) 

            if(opcion1==3):
                os.system("clear")
                eliminar_coders(grupo_codersa)   

            if(opcion1==4):
                os.system("clear")
                mostrar_grupo(grupo_codersa)

            if(opcion1==5):
                actualizar_coders(grupo_codersa)





        if(opcion_grupo==2):

            print("1.Para ingresar datos del coder")
            print("2.Buscar couders")
            print("3.Para eliminar Coders")
            print("4.Mostrar los grupos de coders")
            print("5.Para actualizar datos de couders")

            opcion2=int(input("Sleccione una opcion para continuar: "))

            if(opcion2==1):
                os.system("clear")
                ingresa_datos(grupo_codersb)

            if(opcion2==2):
                os.system=("clear")
                buscar_coders(grupo_codersb) 

            if(opcion2==3):
                os.system("clear")
                eliminar_coders(grupo_codersb)   

            if(opcion2==4):
                os.system("clear")
                mostrar_grupo(grupo_codersb)

            if(opcion2==5):
                actualizar_coders(grupo_codersb)




        if(opcion_grupo==3):

            print("1.Para ingresar datos del coder")
            print("2.Buscar couders")
            print("3.Para eliminar Coders")
            print("4.Mostrar los grupos de coders")
            print("5.Para actualizar datos de couders")

            opcion3=int(input("Sleccione una opcion para continuar: "))

            if(opcion3==1):
                os.system("clear")
                ingresa_datos(grupo_codersc)

            if(opcion3==2):
                os.system=("clear")
                buscar_coders(grupo_codersc) 

            if(opcion3==3):
                os.system("clear")
                eliminar_coders(grupo_codersc)   

            if(opcion3==4):
                os.system("clear")
                mostrar_grupo(grupo_codersc)

            if(opcion3==5):
                actualizar_coders(grupo_codersc)

        if(opcion_grupo==4):
            premiacion(grupo_codersa)

        if(opcion_grupo==5):
            print("FIN DEL PROGRAMA")
            break

main()