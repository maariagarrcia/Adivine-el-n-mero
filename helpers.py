import os

#Limpiar la terminal
#No funciona al ejecutar en ventana interactiva
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

# Valida si una cadena es numero entre min y max
# Devuelve:
#     True----> numero entre min y max
#     False---> No cumple requisitos
def input_usuarioOk(input, min, max):
    ok= False

    try:
        #Convertir el input del usuario a tipo numerico
        numero=int(input)
    except:
        pass #No es un numero
    else:
        if(min<=numero<=max):
            ok= True
     
    return ok