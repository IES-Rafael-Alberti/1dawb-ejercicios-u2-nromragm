def pedir_edad():

    salir = False
    while not salir:
        entrada = input("Introduzca su edad: ")

        if entrada.isnumeric() and 0 < int(entrada):
            salir = True
        else:
            print("La edad introducida no valida.")
    
    edad = int(entrada)

    return edad


def comprobar_edad(edad):

    if edad < 4:
        precio = "Puede entrar gratis"

    elif 4 >= edad >= 18:
        precio = "La entrada vale 5€"

    else:
        precio = "La entrada vale 10€"
        
    return precio


def main():

    edad = pedir_edad()

    resultado = comprobar_edad(edad)

    print(resultado)


if __name__ == "__main__":
    main()