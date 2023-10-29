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


def numeros_impares(numero):
    print(f"Numeros impares hasta {numero} :", end=" ")

    for i in range (1, numero + 1, 2):
        if i != 1:
            print(", ", end="")
        
        print(i, end="")    
    

def main():
    
    numero = pedir_numero()
    
    numeros_impares(numero)


if __name__ == "__main__":
    main()