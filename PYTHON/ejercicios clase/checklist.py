import os


def mostrar_tareas(tareas_diarias):
    if not tareas_diarias:
        print("No hay tareas existentes ")

    else:
        print("Lista de tareas")

        for index, valor in enumerate(tareas_diarias):
            print(index, valor["nombre"], "-",valor["realizada"])





def agregar_tarea(tareas_diarias):

    try: 

        nombre=input("Ingrese el nombre de la tarea: ")
        realizada=input("¿Esta la tarea realiza?: ") 

        tarea={"nombre": nombre,"realizada": realizada} 

        tareas_diarias.append(tarea)

        print("Tarea agregada exitosamente\n")

    except:
        print("Los valores ingresados no son validos")


def actualizar_tarea(tareas_diarias):
    mostrar_tareas(tareas_diarias)

    if not tareas_diarias:
        return

    else:
        try:
            indice=int(input("Ingrese el indice de la tarea a actualizar: "))

            if(indice<0 or indice >len(tareas_diarias)):
                print("El indice ingresado no corresponde a ninguna tarea")

            else:

                nombre=input("Ingrese el nuevo nombre de la tarea: ")
                realizada=input("¿Esta la tarea realizada?")

                tareas_diarias[indice]["nombre"]=nombre
                tareas_diarias[indice]["realizada"]=realizada

                print("¡La tarea fue actualizada con exito!")

        except:
            print("El valor ingresado debe ser un numero")


def buscar_tarea(tareas_diarias):
    mostrar_tareas(tareas_diarias)

    if not tareas_diarias:
        return

    else:

        buscar=input("Ingrese la tarea que quiere buscar: ")

        for index, valor in enumerate((tareas_diarias)):
            if(valor["nombre"].lower()==buscar.lower()):
                print("La tarea es: ", valor["nombre"], "-", valor["realizada"])




def eliminar_tarea(tareas_diarias): 
    mostrar_tareas(tareas_diarias)

    try: 

        eliminar=int(input("Ingrese el indice de la tarea que va a eliminar: "))


        tareas_diarias.pop(eliminar)

        print("Tarea eliminada exitosamente\n")
        print("Tu lista actualizada de tares es: ")
        mostrar_tareas(tareas_diarias)




    except:
        print("Los valores ingresados no son validos")









def main():

    tareas_diarias=[{"nombre": "hacer la cama", "realizada":"si"} ,
                    {"nombre": "Bañarse", "realizada": "si" }]

    while(True):
        print("*****Check list*****")
        print("1.mostrar todos las tareas")
        print("2.Agregar tarea")
        print("3.Actualizar tarea")
        print("4.Buscar tarea")
        print("5.Eliminar tarea")

        opcion=int(input("Elija una opcion: "))

        if (opcion==1):
            os.system("clear")
            mostrar_tareas(tareas_diarias)

        if(opcion==2):
            os.system("clear")
            agregar_tarea(tareas_diarias)

        if(opcion==3):
            os.system("clear")
            actualizar_tarea(tareas_diarias)

        if(opcion==4):
            os.system("clear")
            buscar_tarea(tareas_diarias)

        if(opcion==5):
            os.system("Clear")
            eliminar_tarea(tareas_diarias)



















main()
