def comprobar_edad(edad):

    if edad < 4:
        precio = "Puede entrar gratis"

    elif 4 >= edad >= 18:
        precio = "La entrada vale 5€"

    else:
        precio = "La entrada vale 10€"
        
    return precio


def main():

    edad = int(input("Ingrese su edad: "))

    resultado = comprobar_edad(edad)

    print(resultado)


if __name__ == "__main__":
    main()