import random
#El juego consiste en que el ORDENADOR escoge un número al azar (random)del 0 al 99.
# El jugador tiene que adivinarlo con el  menor número de intentos posible.
# Cada ves que el jugador se equivoca el ORDENADOR le tiene que dar una pista, indicando
# si el número escogido inicialmente es menor o mayoor que el propuest por el JUGADOR.

# Modificando min y max puedes cambiar el rango de numeros del juego
min=0
max=99

# Preparativos antes de empezar el juego
print("Soy el ordenador y voy a pensar un número entre" +  str(min) + "y" +  str(max))
print("Ya lo tengo, ahora tienes que adivinar mi numero secreto")
print("Si te equivocas te doy pistas :) ")

#Variable booleana. Permite que el juego finalice cuando el jugador acierta
encontrado= False
# Cuenta el numero de intentoos que el jugadoor ha realizado
intento=0
#Seleccionar un numero de forma aleatoria
numero_secreto=random.randint(min,max)

#print("Chivato para depuracion. He pensado en el", numero_secreto)
print()
print("---Empieza el juego---")
while not encontrado:
    intento= intento+1
    numero_usuario=int(input("Dime, ¿cual es el numero secreto?"))
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