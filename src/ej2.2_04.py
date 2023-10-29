def pedir_numero():

    salir = False
    while not salir:
        entrada = int(input("Introduze un numero entero positivo: "))

        if entrada > 0:
            salir = True
        
        else:
            print("El numero introducido no es valido.")
    
    numero = int(entrada)

    return numero


def cuenta_atras(numero):
    print(f"Cuenta atras hasta 0 desde {numero}:", end=" ")
    
    while numero >= 0:
        if numero != 0:
            print(numero, end=", ")
        
        else:
            print(numero, end=".")
        numero -= 1  
    

def main():
    
    numero = pedir_numero()
    
    cuenta_atras(numero)


if __name__ == "__main__":
    main()