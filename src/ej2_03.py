def division(numero, divisor):
    
    if divisor == 0:
        resultado = "Error: No se puede dividir por cero."
    else:
        resultado = str(numero / divisor)
    
    return resultado    


def main():

    num = float(input("Introduce un numero: "))
    divi = float(input("Introduce el divisor: "))

    resultado = division(num, divi)
    print(f"{resultado}")


if __name__ == "__main__":
    main()
    