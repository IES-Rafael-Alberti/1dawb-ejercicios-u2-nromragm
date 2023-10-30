from ej22_03 import pedir_numero


def triangulo_rectangulo(numero):
        
    for i in range(1, numero + 1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print()

def main():
    
    numero = pedir_numero()
    
    triangulo_rectangulo(numero)


if __name__ == "__main__":
    main()