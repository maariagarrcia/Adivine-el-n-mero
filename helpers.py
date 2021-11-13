import os
#No funciona al ejecutar en ventana interactiva
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

# Valida si una cadena es numero entre min y max
# Devuelve:
#           True----> numero entre min y max
#           False---> No cumple requisitos
def input_usuarioOk(input, min, max):
    ok=False

    try:
              numero_usuario=int(input("Dime, ¿cual es el numero secreto?"))
    except:
        print("Solo acepto numeros. Vuelve a intentarlo")
        pass #No es un numero
    else:
        if(min<=numero_usuario<=max):
                ok= True
        
    return ok