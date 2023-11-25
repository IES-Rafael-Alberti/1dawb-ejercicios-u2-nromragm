def pedir_password():
    contraseña_usuario = input("Ingresa la contraseña: ")
    
    return contraseña_usuario


def validar_password(contraseña_usuario):

    contraseña = "contraseña"

    if contraseña == contraseña_usuario.lower():
        return True
    else:
        return False



def main():
    contraseña_usuario = pedir_password()
    
    if validar_password(contraseña_usuario):
        print("La contraseña es correcta.") 
    else:
        print("La contraseña es incorrecta.")



if __name__ == "__main__":
    main()
