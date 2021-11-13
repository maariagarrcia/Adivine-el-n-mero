import helpers
import menu
from colorama import Fore, Back

def aceptar_opcion_menu():
    opcion= -1
    salir: False

    while (not  salir):
        inputusuario= input(Fore. GREEN + "Dime que opcion deseas" + Fore.WHITE)
          
        if (inputusuario== "F" or inputusuario == "f"):
             # Finalizar
            opcion=-1
            salir= True
        elif (inputusuario== " P" or inputusuario== "p"):
            # Ver puntuaciones
            opcion=-2
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