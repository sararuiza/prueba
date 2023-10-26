

def maximo(municipios):

    if not municipios:
        print("No hay municipios registrados")

    max_toneladas=0
    nombre_max_tonelada=""

    for valor in municipios:
        if valor[1] > max_toneladas:
            max_toneladas = valor[1]
            nombre_max_toneladas = valor[0]
            
    





def main():

    municipios =[
        ["Rionegro",1000,50,20,30],
        ["Puerto Berrio",2000,20,50,30],
        ["Guatape",6000,30,40,30],
        ["Envigado",2000,30,30,40],
        ]

    opcion=int(input("1 para maximo\n 2 para minimo \n 3 para promedio"))

    if(opcion==1):
        maximo(municipios)




main()