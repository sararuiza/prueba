import os

def datos_municipios(municipios):
#P1 problematica 1 olores ofensivos
#P2 problematica 2 asentamientos ilegales
#P3 problematica 3 contaminacion fuentes hidricas
    try:

        nombre_municipio=input("Ingrese el nombre del municipio: ")
        toneladas_dia=int(input("Ingrese el numero de toneladas por dia que generan: "))
        print("Señor usuario a continuacion usted reportara los valores")
        print("de las problematicas ambientales en el municipio, estos valores")
        print("son porcentajes de 1 a 100 y la suma de los 3, debe ser igual a 100")
        input("Presione enter para continuar: ")
        print("PROBLEMAS AMBIENTALES")
        olores_ofensivos=int(input("Ingrese el porcentaje de 1 a 100 de olores ofensivos reportador: "))
        asentamientos_ilegales=int(input("Ingrese el porcentaje de 1 a 100 de asentamientos ilegales reportador: "))
        contaminacion_hidricos=int(input("Ingrese el porcentaje de 1 a 100 de la contaminacion hidricos reportador: "))

        porcentaje=olores_ofensivos+asentamientos_ilegales+contaminacion_hidricos

        if(porcentaje==100):
            print("el porcentaje se divide: ")
            print("olores ofensivos", olores_ofensivos)
            print("asentamiento ilegales", asentamientos_ilegales)
            print("contaminacion de fuentes hidricas", contaminacion_hidricos)

        else:
            print("valores ingresados no son correctos")

    except:
        return


def mostrar_lista(municipios):

    if not municipios:
        print("No hay minucipios registrados")

    else:
        print("MUNICIPIOS")

        for index,valor in enumerate(municipios):
            print(index, valor["nombre_municipio"],"-", valor["toneladas_dia"],"- P1", valor["olores_ofensivos"],"- P2", valor["asentamientos_ilegales"],"- P3",valor["contaminacion_hidricos"])
            #print(municipios)


def actualizar_municipios(municipios):
    mostrar_lista(municipios)

    if not municipios:
        return
    
    else:

        try:

            indice=int(input("Ingrese el indice del municipio que va a actualizar: "))
            
            if(indice<0 or indice>len(municipios)):
                print("El indice ingresado no corresponde a ningun municipio")

            else:
                nombre_nuevo=input("Ingrese el nuevo nombre del municipio: ")
                toneladas_nuevo=input("Ingrese las toneladas dia: ")
                olores_nuevo=input("Ingrese el procentaje de olores ofensivos: ")
                asentamientos_nuevo=input("Ingrese el porcentaje de asentamientos ilegales: ")
                contaminacion_hidrico=input("Ingrese el porcentaje de cintaminacion hidrica: ")

                municipios[indice]["nombre:municipio"]=nombre_nuevo
                municipios[indice]["toneladas_dia"]=toneladas_nuevo
                municipios[indice]["olores_ofensivos"]=olores_nuevo
                municipios[indice]["asentamientos_ilegales"]=asentamientos_nuevo
                municipios[indice]["contaminacion_hidricos"]=contaminacion_hidrico

                print("Municipio actualizado exitosamente")
        except:
            print("El valor ingresado no es correcto")


def eliminar_municipios(municipios):
    mostrar_lista(municipios)

    eliminar=int(input("Ingrese el indice que desea eliminar: "))

    municipios.pop(eliminar)
    print("Municipio elimindo exitosamente")


def toneladas_dia(municipios):

    # suma=0
    # for index, valor in enumerate(municipios):

    #     suma=suma+valor["toneladas_dia"]
    
    # print(suma/len(municipios))


#def municipio_mas_toneladas(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    max_toneladas = 0
    nombre_max_toneladas = ''
    
    for index, valor in enumerate(municipios):
        if valor["toneladas_dia"] > max_toneladas:
            max_toneladas = valor["toneladas_dia"]
            nombre_max_toneladas = valor["nombre_municipio"]
    print("\nEl municipio que más toneladas/día genera es",nombre_max_toneladas,"con",max_toneladas,"toneladas.\n")
   

    






    
def main():

    municipios=[{"nombre_municipio":"rio negro", "toneladas_dia": int(1200),"olores_ofensivos": int(37), "asentamientos_ilegales": int(23), "contaminacion_hidricos": int(40)},
                {"nombre_municipio":"retiro", "toneladas_dia": int(1350),"olores_ofensivos": int(20), "asentamientos_ilegales": int(15), "contaminacion_hidricos": int(65)},
                {"nombre_municipio":"la ceja", "toneladas_dia": int(1240),"olores_ofensivos": int(17), "asentamientos_ilegales": int(33), "contaminacion_hidricos": int(50)}]


    while (True):

        input("Presione enter para iniciar: ")
        print("Bienvenido al modulo de control de basura")
        print("1. Para ingresar municipio")
        print("2. Para mostrar municipios")
        print("3. Para actualizar municipios")
        print("4. Para eliminar municipios")
        print("5. Toneladas dia/genera ")
    #menos- mas- prormedio
        print("6.Problematica ambiental")
    #mas y menos 
        print("7.Creacion de acentamientos")
    #mas, menos- promedio
        print("8.Contaminacion de corrientes hidricas")
    #mas, menos- promedio

        opcion=int(input("Presione una opcion para continuar: "))

        if(opcion==1):
            datos_municipios(municipios)

        if(opcion==2):
            mostrar_lista(municipios)

        if(opcion==3):
            actualizar_municipios(municipios)

        if(opcion==4):
            eliminar_municipios(municipios)

        if(opcion==5):
            toneladas_dia(municipios)



main()
