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
        elif (inputusuario== "p" or inputusuario== "p"):
            # Ver puntuaciones
            opcion=2
        elif input_usuarioOk(inputusuario, 1,4):
                #JUGAR CON NIVEL ENTRE 1,4
                salir= True
        else:
            # Opcion incorrecta
            print(Fore.RED + "*ATENCION: Seleccione una opcion valida" + Fore.WHITE )
    
    return opcion

def menu():
    print()
    print(Fore.GREEN + "MENU")
    print("----")
    print("1 - Jugar al Nivel mas facil, el 1")
    print("2 - Jugar al Nivel 2")
    print("3 - Jugar al Nivel 3")
    print("4 - Jugar al Nivel 4, el mas dificil")
    print("P - Ver puntuaciones")
    print("F - Finalizar")
    print(Fore.WHITE)

    opcion=aceptar_opcion_menu()
    return opcion

# Acepta un numero entre min y max,  F para finalizar o A para solicitar ayuda
# Un numero valido y correcto
# o un -1 si se ha introducido una F
# o un -2  si se ha introducido una A

def aceptarjugada(min, max):
    jugada= -1
    salir= False

    while (not salir):
        inputusuario= input(Fore.YELLOW+ "Dime cual crees que es el numero secreto")
        if(inputusuario == "F" or inputusuario == "F"):
            jugada:-1
            salir: True
        elif (inputusuario=="A" or inputusuario== "a"):
            jugada:-2
            salir: True
        else:
            if input_usuarioOk(inputusuario, min,max):
                jugada:int(inputusuario)
                salir: True
            else:
                print(
                        Fore.RED + "*ATENCION: Solo acepto numeros (entre" +
                        Fore.WHITE + str(min)+
                        Fore.RED + "y" +
                        Fore.WHITE +str(max) +
                        Fore.RED + "o" +
                        Fore.WHITE + "F" +
                        Fore.RED  + "(finalizar) o " +
                        Fore.WHITE + "A" +
                        Fore.RED + "(pedir ayuda)...")
    return  jugada


def mostrarayuda():
    pass

def avisariniciopartida(min, max, numero_secreto, depurar):
    if (depurar):
        print(Fore.CYAN)
        print("Chivato para depuracion. He pensado en el", numero_secreto)

 #Preparativos antes de empezar
    print(Fore.YELLOW)
    print(" Soy el ordenador y voy a pensar un número entre " +  str(min) + " y " +  str(max))
    print("Ya lo tengo, ahora tienes que adivinar mi numero secreto")
    print("Si te equivocas te doy pistas :) ")
    print(Fore.RED + "Durante el juego puedes obtener ayuda pulsando A" + Fore.Yellow)
    print("Empieza  la partida")


def avisarfinpartida(numero_secreto, intento, maxintentos, encontrado, finalizar):
    print(Fore.YELLOW+ "El juego  ha finalizado :(")
    print()


    if(encontrado):
        print(Fore. RED+"Genial,  lo has adivinado en o has adivinado en " + str(intento) + " intentos ")
    elif(finalizar):
        print("Ya veo  que no quieres continuar con la partida :/")
    elif(intento >= maxintentos):
        print("Has realizado"  + str(intento) + "intentos")

    print("El numero que había pensado es el " + str(numero_secreto))
    print("Has realizad" + str(intento) + "intentos")

def mostrarpista(minactual, maxactual):
    print(
        Fore.RED + "*Pista: El numero secreto debe estar entre" +
        Fore.White +str(minactual) +
        Fore.RED + "y" +
        Fore.White + str (maxactual)
    )
# Donde se guardan las listas
def actualizarPuntuaciones(diccionarioPuntuaciones):
    print(Fore.WHITE)
    print("Actualizacion de puntuaciones")
    nombreJugador= input("Dime tu nombre")
    if(nombreJugador in diccionarioPuntuaciones):
        #Si el jugador existe en el diccionario apuntar una partida mas
        diccionarioPuntuaciones [nombreJugador] = diccionarioPuntuaciones[nombreJugador] + 1
    else:
        #Caso de no existir se añadira un item al diccionario
        diccionarioPuntuaciones[nombreJugador] =1
    
def mostrarPuntuaciones (diccionarioPuntuaciones):
    print(Fore. WHITE)
    print("Lista de partidas ganadas")
    print(diccionarioPuntuaciones)

def jugar(min,max, maxIntentos, puntuaciones):
    clear()

    numero_secreto=random.randint(min,max)
    avisariniciopartida(min,max,numero_secreto, True)
    intento=0          #Contador de numero de intentos
    encontrado= False  #Indica que se ha adivinado el numero
    finalizar= False   #Indica que el usuario quiere  finalizar la partida
    minActual= min     #Minimo que ya sabemos que puede ser el secreto
    maxActual=  max    #Es el maxim que ya sabemos que puede ser el secreto

    while (not finalizar and not encontrado and intento < maxIntentos):
        numero_usuario= aceptarjugada(min,max)
        if(numero_usuario == -1):
            finalizar= True
        elif (numero_usuario == -2):
            mostrarpista(minActual, maxActual)
        else:
            intento= intento+1
            #Comprobar si el jugadoor ha acertado el numero
            encontrado=(numero_usuario==numero_secreto)
            if(numero_usuario>numero_secreto):
                maxActual=numero_usuario
                print(Fore.YELLOW +  "El"  +str(numero_usuario)+ " es MAYOR que el numero secreto")
            elif(numero_usuario<numero_secreto):
                minActual= numero_usuario
                print(Fore. YELLOW + " El " + str(numero_usuario) + " es MENOR que el numero secreto")
   
    avisarfinpartida(numero_usuario, intento, maxIntentos, encontrado, finalizar)
    
    if(encontrado):
        actualizarPuntuaciones(diccionarioPuntuaciones)




    
    


