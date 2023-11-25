def pedir_numero():
    numero = int(input("Introduce un numero entero positivo (o -1 para terminar): "))
    return numero

def suma_digitos(numero):
    suma = 0
    
    for i in str(numero):
        suma += int(i)
    
    return suma

def main():
    numeros_pares = 0
    salir = False
    
    while not salir:
        numero  = pedir_numero()
        
        if numero == -1:
            salir = True
        
        else:

            suma = suma_digitos(numero)
        
            print(f"La suma de los digitos es {suma}")
        
            if suma % 2 == 0:
                numeros_pares += 1

    print(f"Se introducieron {numeros_pares} numeros pares.")

if __name__ == "__main__":
    main()