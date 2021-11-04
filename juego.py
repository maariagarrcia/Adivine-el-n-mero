import random

#El juego consiste en que el ORDENADOR escoge un número al azar (random)del 0 al 99.
# El jugador tiene que adivinarlo con el  menor número de intentos posible.
# Cada ves que el jugador se equivoca el ORDENADOR le tiene que dar una pista,  indicando
# si el número escogido inicialmente es menor o mayoor que el propuest por el JUGADOR.
 
numero_aleatorio=random.randint(min,max)
min=0
max=99
numero_aleatorio= int

print("Soy el ordenador y voy a pensar un número entre" +str(min) +"y"str(max))
print("Ya lo tengo, ahora tienes que adivinar mi numero secreto")
print("Si te equivocas te doy pistas :) ")

while True:
    if 0<numero_aleatorio<99:
        print("Numero entre los valores 0 y 99")
    break

while True:
    numero_usuario= input()
    if 0<=numero_usuario<=99:
        print(numero_usuario)
    else:
        pass
    break


while numero_aleatorio==numero_usuario:
    if numero_aleatorio>numero_usuario:
        print("Demasiado grande")
    else:
        print("Demasiado pequeño")
    if numero_aleatorio==numero_usuario:
        print("Has ganado")