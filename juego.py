import random
numero_aleatorio=random.randint(0,100)
numero_aleatorio= int
print (numero_aleatorio)

print("piensa un número entre" + str(min) + str(max))

numero_usuario= input()

while numero_aleatorio==numero_usuario:
    if numero_aleatorio>numero_usuario:
        print("Demasiado grande")

    else:
        print("Demasiado pequeño")

    if numero_aleatorio==numero_usuario:
        print("Has ganado")




