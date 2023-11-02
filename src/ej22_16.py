def pedir_numero():
    
    numero = int(input("Introduce un numero entero o 0 para terminar: "))
    
    return numero


def main():
    
    salir  = False
    
    mayor = 0

    while not salir:
        numero = pedir_numero()
        
        if numero == 0:
            salir  = True
        
        elif mayor < numero:
            mayor = numero
    
    print(f"El mayor de los numeros es: {mayor}")


if __name__ == "__main__":
    main()