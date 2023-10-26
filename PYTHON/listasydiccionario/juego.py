import random



def juego(preguntas):
  
    contador=0
    while True:
        
        numero= random.randint(0,5)
        print(preguntas[numero]["pregunta"])
        for i, value in enumerate(preguntas[numero]["opciones"]):
            print(i+1, value)
        respuesta=(input("Selecciones la respuesta correcta: "))
        if(respuesta==preguntas[numero]["respuesta"]):
            print("Respuesta correcta")
            contador=contador+1
            print(contador)

        else:
            print("respuesta incorrecta")
        opcion = int(input("Quieres continuar:"))




def main():

    preguntas = [
        {"pregunta": "Cual es el simbolo quimico del mercurio",
         "opciones": ["A.Mg", "B.O", "C.Hg", "D.F"],
         "respuesta": "C"},

        {"pregunta": "Cual es el simbolo quimico del oro",
         "opciones": ["A.Al", "B.P", "C.Hg", "D.Au"],
         "respuesta": "D"},

        {"pregunta": "Cual es el simbolo quimico del azufre",
         "opciones": ["A.S", "B.H", "C.He", "D.B"],
         "respuesta": "A"},

        {"pregunta": "Cual es el simbolo quimico del helio",
         "opciones": ["A.Mg", "B.He", "C.Hg", "D.F"],
         "respuesta": "B"},

        {"pregunta": "Cual es el simbolo quimico del Boro",
         "opciones": ["A.Mg", "B.O", "C.Hg", "D.B"],
         "respuesta": "D"}
    ]

    print("****************")
    print("***BIENVENIDO***")
    print("****************")
    print("1. Para ingresar al juego")
    print("2.Para salir del juego")

    opcion=int(input("Elija una opcion: "))

    if(opcion==1):
        juego(preguntas)
    


    

    


main()
