from ej22_14 import pedir_numero


def main():
    
    suma = 0
    
    salir  = False
    
    while not salir:
        numero = pedir_numero()
        
        if numero == 0:
            salir  = True
        
        elif numero > 0:
            suma += numero
    
    print(f"La suma de los numeros positivos es: {suma}")


if __name__ == "__main__":
    main()