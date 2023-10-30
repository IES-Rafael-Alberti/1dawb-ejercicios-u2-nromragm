from ej22_03 import pedir_numero

def numero_es_primo(numero):
    for i in range(2, numero):
        
        if (numero % i) == 0:
            return False
       
        else:
            return True


def main():
    numero = pedir_numero()

    if numero_es_primo(numero):
        print("El numero es primo")

    else:
        print("El numero no es primo")    



if __name__ == "__main__":
    main()