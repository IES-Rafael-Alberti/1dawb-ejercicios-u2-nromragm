def pedir_numero():
    while True:
        numero = int(input("Introduce un numero entero positivo (o 0 para finalizar): "))
        
        if numero >= 0:
            return numero
        
        if numero < 0:
            resultado = "ERROR Ingresa un numero positivo."
            return resultado


def par_impar(numero):
    pares = 0
    impares = 0
    
    for digito in str(numero):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares


def main():
    numero = None
    total_pares = 0
    total_impares = 0
    
    while numero != 0:
        numero = pedir_numero()
        pares, impares = par_impar(numero)
        print(f"El numero {numero} tiene {pares} digitos pares y {impares} impares")
        
        total_pares += pares
        total_impares += impares

    print(f"En total se leyeron {total_pares} digitos pares y {total_impares} impares.")

if __name__ == "__main__":
    main()
