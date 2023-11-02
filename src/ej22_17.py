def pedir_numero():
    
    numero = input("Introduce un numero entero: ")
    
    return numero



def suma_digitos(numero):
    
    digitos = [int(digito) for digito in numero]

    suma_digitos = sum(digitos) 

    return suma_digitos


def main():

    numero = pedir_numero()

    resultado = suma_digitos(numero)
    
    print(f"La suma de los digitos es: {resultado}")


if __name__ == "__main__":
    main()