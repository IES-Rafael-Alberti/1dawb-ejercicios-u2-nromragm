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


def años_cumplidos(edad):
    
    print("Años que has cumplido: ")
    
    for i in range (1, edad + 1):
        print(i)


def main():
    
    edad = pedir_edad()
    
    años_cumplidos(edad)


if __name__ == "__main__":
    main()