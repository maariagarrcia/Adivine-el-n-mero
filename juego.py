import random
#El juego consiste en que el ORDENADOR escoge un número al azar (random)del 0 al 99.
# El jugador tiene que adivinarlo con el  menor número de intentos posible.
# Cada ves que el jugador se equivoca el ORDENADOR le tiene que dar una pista, indicando
# si el número escogido inicialmente es menor o mayoor que el propuest por el JUGADOR.
 
min=0
max=99


print("Soy el ordenador y voy a pensar un número entre" +  str(min) + "y" +  str(max))
print("Ya lo tengo, ahora tienes que adivinar mi numero secreto")
print("Si te equivocas te doy pistas :) ")

encontrado= False
intento=0
numero_secreto=random.randint(min,max)
print("He pensado en el", numero_secreto)

while not encontrado:
    intento= intento+1
    numero_usuario= int(input("Dime, ¿cual es el numero secreto?"))
    encontrado=(numero_secreto==numero_usuario)
    print("intento" +str(intento)+'>', end="")
    
    if(encontrado):
        print("Has ganado")
    elif(numero_secreto>numero_usuario):
        print("Demasiado grande. El "+str(numero_usuario)+" es mayor que numero secreto")
    else:
        print("Demasiado pequeño. El " + str(numero_usuario) + " es menor que numero secreto")

print("\n>>>>> Lo has adivinado en"+str(intento) + "intentos <<<<<")
print("El numero que había pensado es el " + str(numero_secreto))