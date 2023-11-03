from ej2_02 import pedir_password

from ej2_02 import validar_password


def main():

    salir = False
    while not salir:
        contraseña_usuario = pedir_password()
        
        if validar_password(contraseña_usuario):
            print("La contraseña es correcta.")
            
            salir = True
        
        else:
            print("La contraseña es incorrecta.")


if __name__ == "__main__":
    main()  