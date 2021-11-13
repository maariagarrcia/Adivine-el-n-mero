# PAGINAS CONSULTADAS
#
# Uso funciones...... https://www.w3schools.com/python/python_functions.asp
# Como devolver multiples valores con una funcion.... https://www.tutorialspoint.com/returning-multiple-values-in-python
# Comoo limpiar terminal.... https://www.micro.recursospython.com/recursos/como-limpiar-la-consola.html
#  Como imprimir colores en la terminal.... https://pypi.org/project/colorama/
# Uso diccionarios.... https://pythonexamples.org/python-dictionary-operations/
# Uso modulo.... https://www.w3schools.com/python/python_modules.asp

import random
import helpers
import menu
from colorama import Fore, Back

# F U N C I O N E S


# Acepta un numero entre min y max,  F para finalizar o A para solicitar ayuda
# Un numero valido y correcto
# o un -1 si se ha introducido una F
# o un -2  si se ha introducido una A

def aceptarjugadapersona(min, max):
    jugada= -1
    salir= False

    while (not salir):
        inputusuario= input(Fore.YELLOW + "Dime cual crees que es el numero secreto")
        
        if(inputusuario == "F" or inputusuario == "f"):
            jugada= -1
            salir= True
        elif (inputusuario== "A" or inputusuario== "a"):
            jugada= -2
            salir= True
        else:
            if helpers.input_usuarioOk(inputusuario, min,max):
                jugada=int(inputusuario)
                salir= True
            else:
                print(
                    Fore.RED + '* ATENCION: Solo acepto números (entre ' + 
                    Fore.WHITE + str(min) + 
                    Fore.RED + ' y ' + 
                    Fore.WHITE + str(max) + 
                    Fore.RED + ') o ' + 
                    Fore.WHITE + '"F"' + 
                    Fore.RED + ' (finalizar) o '+
                    Fore.WHITE + '"A"' +
                    Fore.RED + ' (pedir ayuda) ...')
    return jugada


def avisariniciopartida(min, max, numero_secreto, depurar):
    if (depurar):
        print(Fore.CYAN)
        print("Chivato para depuracion. He pensado en el", numero_secreto)

 #Preparativos antes de empezar
    print(Fore.YELLOW)
    print()
    print(" Soy el ordenador y voy a pensar un número entre " +  str(min) + " y " +  str(max))
    print("Ya lo tengo, ahora tienes que adivinar mi numero secreto")
    print("Si te equivocas te doy pistas :) ")
    print(Fore.RED + "Durante el juego puedes obtener ayuda pulsando A" + Fore.YELLOW)
    print("Empieza  la partida")

    
def avisarfinpartida(numero_secreto, intento, maxintentos, encontrado, finalizar):
    print(Fore.YELLOW+ " El juego  ha finalizado :( ")
    print()


    if(encontrado):
        print(Fore. RED + "Genial,  lo has adivinado en o has adivinado en " + str(intento) + " intentos ")
    elif(finalizar):
        print("Ya veo  que no quieres continuar con la partida :/")
    elif(intento >= maxintentos):
        print("Has realizado"  + str(intento) + "intentos")

    print("El numero que había pensado es el " + str(numero_secreto))
    print("Has realizado" + str(intento) + "intentos")

def mostrarayuda(minactual, maxactual):
    print(
        Fore.RED + "*Pista: El numero secreto debe estar entre" +
        Fore.WHITE +str(minactual) +
        Fore.RED + "y" +
        Fore.WHITE + str (maxactual)
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
    print(Fore.WHITE)
    print("Lista de partidas ganadas")
    print(diccionarioPuntuaciones)

def aceptarJugadaMasterIA(minActual, maxActual):
    jugadaIA=int((maxActual+minActual)/2)
    print(jugadaIA)
    return jugadaIA

def jugar(min,max, maxIntentos, diccionarioPuntuaciones, usarIA):
    helpers.clear()

    numero_secreto=random.randint(min,max)
    avisariniciopartida(min,max,numero_secreto, True)
    intento=0          #Contador de numero de intentos
    encontrado= False  #Indica que se ha adivinado el numero
    finalizar= False   #Indica que el usuario quiere  finalizar la partida
    minActual= min     #Minimo que ya sabemos que puede ser el secreto
    maxActual=  max    #Es el maxim que ya sabemos que puede ser el secreto

    while (not finalizar and not encontrado and intento < maxIntentos):
        if (usarIA):
            mostrarayuda(minActual, maxActual)
            numero_usuario=aceptarJugadaMasterIA(minActual, maxActual)
        else:
            numero_usuario= aceptarjugadapersona(min,max)
        if(numero_usuario == -1):
            finalizar= True
        elif (numero_usuario == -2):
            mostrarayuda(minActual,maxActual)
        else:
            intento= intento +1
            #Comprobar si el jugador ha acertado el numero
            encontrado= (numero_usuario==numero_secreto)
            if(numero_usuario>numero_secreto):
                maxActual=numero_usuario
                print(Fore.YELLOW +  "El"  +str(numero_usuario)+ " es MAYOR que el numero secreto")
            elif(numero_usuario<numero_secreto):
                minActual= numero_usuario
                print(Fore. YELLOW + " El " + str(numero_usuario) + " es MENOR que el numero secreto")
   
    avisarfinpartida(numero_secreto, intento, maxIntentos, encontrado, finalizar)
    
    if(encontrado):
        actualizarPuntuaciones(diccionarioPuntuaciones)

# INICIO PROGRAMA

diccionarioPuntuaciones= {}

helpers.clear() #Limpia la terminal
finalizar= False
while (not finalizar):
    opcion = menu.menu()

    if (opcion==1):
        jugar(0, 100, 10, diccionarioPuntuaciones, False)
    elif (opcion==2):
        jugar(0,1000, 20, diccionarioPuntuaciones, False)
    elif (opcion==3):
        jugar(0,10000, 30, diccionarioPuntuaciones, False)
    elif (opcion==4):
       jugar(0,100000, 40, diccionarioPuntuaciones, False)
    elif (opcion==5):
        jugar(0, 10000000,  50, diccionarioPuntuaciones, True)
    elif (opcion==-1): #Salir
        finalizar= True
    elif (opcion==-2): #Ver puntuaciones
        mostrarPuntuaciones(diccionarioPuntuaciones)

print(Fore.GREEN  + "Nos vemos otro dia :)")
print(Fore.WHITE)







    
    


