# PAGINAS CONSULTADAS
#
# Uso funciones...... https://www.w3schools.com/python/python_functions.asp
# Como devolver multiples valores con una funcion.... https://www.tutorialspoint.com/returning-multiple-values-in-python
# Comoo limpiar terminal.... https://www.micro.recursospython.com/recursos/como-limpiar-la-consola.html
#  Como imprimir colores en la terminal.... https://pypi.org/project/colorama/
# Uso diccionarios.... https://pythonexamples.org/python-dictionary-operations/
# Uso modulo.... https://www.w3schools.com/python/python_modules.asp

import random
import os
from colorama import Fore, Back


# F U N C I O N E S

#Limpiar terminal
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
            pass
        else:
            if(min<=numero_usuario<=max):
                ok= True
            else:
                print("Solo acepto numeros entre " + str(min) + " y " + str(max))
        return ok

def aceptar_opcion_menu():
    opcion= -1
    salir: False

    while (not  salir):
        inputusuario= input(Fore. GREEN + "Dime que opcion deseas" + Fore.WHITE)
          
        if (inputusuario== "F" or inputusuario == "f"):
             # Finalizar
            opcion=1
            salir= True
        elif (inputusuario== "p" or inputusuario== "p")
            # Ver puntuaciones
            opcion=2
        else:
            if input_usuarioOk(inputusuario, 1,4):
                #JUGAR CON NIVEL ENTRE 1,4
                salir= True
            else:
                # Opcion incorrecta
                print(Fore.RED + "*ATENCION: Seleccione una opcion valida" + Fore.WHITE )
    
    return opcion

def menu():
    print()
    print(Fore.GREEN + "MENU")
    print("1 Jugar al Nivel mas facil, el 1")
    print("2 Jugar al Nivel 2")
    print("3 Jugar al Nivel 3")
    print("4 Jugar al Nivel 4, el mas dificil")

    opcion=aceptar_opcion_menu()
    return opcion




print(" Soy el ordenador y voy a pensar un número entre " +  str(min) + " y " +  str(max))
print("Ya lo tengo, ahora tienes que adivinar mi numero secreto")
print("Si te equivocas te doy pistas :) ")

# Variable booleana. Permite que el juego finalice cuando el jugador acierta
encontrado= False
# Cuenta el numero de intentos que el jugadoor ha realizado
intento=0
# Seleccionar un numero de forma aleatoria
numero_secreto=random.randint(min,max)

# Este chivatoo me muestra el numero secreto para que sea mas facil depurar el programa
# Una vez funcione el programa  hay que comentarloo
#print("Chivato para depuracion. He pensado en el", numero_secreto)
#Empieza el juego y acabara cuando haya sido adivinado  el numero
print()
print("---Empieza el juego---")
while not encontrado:
    intento= intento+1
    #Ahora vamos  a poner las siguientes condiciones:
    #   Tiene que ser un numero ya que podria  el usuario introducir letras
    #   Tiene que ser entre  el  0 y el 100 (min, max)
    
    #Comparo el numero de usuario con el numero secreto y si son iguales  la variable
    #"encontrado"  valdra verdadero
    encontrado=(numero_secreto==numero_usuario)
    print("intento" +str(intento)+'>', end="")
    
    if(encontrado):
        print("Has ganado")
    elif(numero_usuario>numero_secreto):
        print("Demasiado grande.7 El " +str(numero_usuario)+ " es MAYOR que el numero secreto")
    else:
        print("Demasiado pequeño. El " + str(numero_usuario) + " es MENOR que el numero secreto")

print("---El juego ha finalizado---")
print()
print(" El numero que había pensado es el " + str(numero_secreto) + " y lo has adivinado en " + str(intento) + " intentos ")
