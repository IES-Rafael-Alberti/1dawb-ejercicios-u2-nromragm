def pedir_algo():
   
    entrada = input("Escribe algo (salir para terminar): ")
    
    return entrada


def eco(entrada):

    if entrada.lower() == "salir":
        
        return False
    
    else:
        print(entrada)
        
        return True


def main():
    
    salir = False
    
    while not salir:
        entrada = pedir_algo()
        
        if not eco(entrada):
            salir = True


if __name__ == "__main__":
    main()