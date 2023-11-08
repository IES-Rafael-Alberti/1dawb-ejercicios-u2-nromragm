from ej22_03 import pedir_numero


def triangulo_rectangulo(numero):
    resultado = ""
    for numero in range(1, numero + 1):
        resultado += "*" *  numero + "\n"
    
    return resultado    
    

def main():
    
    numero = pedir_numero()
    
    print(triangulo_rectangulo(numero))


if __name__ == "__main__":
    main()