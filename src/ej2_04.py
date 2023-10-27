def par_o_impar(numero):

    if numero % 2 == 0:
        resultado = "El numero es par"
    else:
        resultado = "El numero es impar"

    return resultado


def main():

    num = int(input("Ingrese un numero entero: "))
    resultado = par_o_impar(num)
    
    print(resultado)


if __name__ == "__main__":
    main()