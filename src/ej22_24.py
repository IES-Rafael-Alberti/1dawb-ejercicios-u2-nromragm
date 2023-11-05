def pedir_numero():
    numero = int(input("Introduce un numero positivo (o 0 para terminar): "))

    return numero


def numero_es_primo(numero):
    for i in range(2, numero):
        
        if (numero % i) == 0:
            return False
       
        else:
            return True

def main():
    numero = pedir_numero()
    primos = 0
    while numero != 0:

        if numero > 1:
            if numero_es_primo(numero) == True:
                primos += 1

            numero = pedir_numero()

        else:
            print("El numero tiene que ser mayor que 1")
            numero = pedir_numero()


    print(f"Se introdujeron {primos} numeros primos")    



if __name__ == "__main__":
    main()
        