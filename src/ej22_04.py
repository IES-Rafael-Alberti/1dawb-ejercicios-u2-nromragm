from ej22_03 import pedir_numero


def cuenta_atras(numero):
    resultado = ""
    print(f"Cuenta atras hasta 0 desde {numero}:", end=" ")
    while int(numero) > 0:
        if numero != 0:
            print(numero, end=", ")

        numero -= 1  
    
    resultado = str(numero) + "."
    
    return resultado


def main():
    
    numero = pedir_numero()
    
    print(cuenta_atras(numero))


if __name__ == "__main__":
    main()