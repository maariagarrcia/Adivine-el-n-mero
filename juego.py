import random

#El juego consiste en que el ORDENADOR escoge un número al azar (random)del 0 al 99.
# El jugador tiene que adivinarlo con el  menor número de intentos posible.
# Cada ves que el jugador se equivoca el ORDENADOR le tiene que dar una pista, indicando
# si el número escogido inicialmente es menor o mayoor que el propuest por el JUGADOR.

# Modificando min y max puedes cambiar el rango de numeros del juego
min=0
max=99

# Preparativos antes de empezar el juego
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
print("Chivato para depuracion. He pensado en el", numero_secreto)
#Empieza el juego y acabara cuando haya sido adivinado  el numero
print()
print("---Empieza el juego---")
while not encontrado:
    intento= intento+1
    #Ahora vamos  a poner las siguientes condiciones:
    #   Tiene que ser un numero ya que podria  el usuario introducir letras
    #   Tiene que ser entre  el  0 y el 100 (min, max)
    while True:
        try:
              numero_usuario=int(input("Dime, ¿cual es el numero secreto?"))
        except:
            print("Solo acepto numeros. Vuelve a intentarlo")
            pass
        else:
            if(min<=numero_usuario<=max):
                break
            else:
                print("Solo acepto numeros entre " + str(min) + " y " + str(max))
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