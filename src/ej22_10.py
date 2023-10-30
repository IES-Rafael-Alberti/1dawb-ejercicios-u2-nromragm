from ej22_03 import pedir_numero

def numero_es_primo(numero):
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
        else:
            return True



    es_primo = True
    for i in range(2, numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")



def main():
    numero = pedir_numero

    if numero_es_primo(numero):
        print("El numero es primo")

    else:
        print("El numero no es primo")    



if __name__ == "__main__":
    main()