import random
numero_aleatorio=random.randint(0,100)
numero_aleatorio= int
print (numero_aleatorio)
intento=0
intentos= intento+1
numero_usuario=int

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