def pedir_numero():
    
    numero = int(input("Introduce un numero entero o 0 para terminar: "))
    
    return numero


def main():
    
    suma = 0
    
    salir  = False
    
    while not salir:
        numero = pedir_numero()
        
        if numero == 0:
            salir  = True
        
        else:
            suma += numero
    
    print(f"La suma de los numeros es: {suma}")


if __name__ == "__main__":
    main()