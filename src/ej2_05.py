def tributar_impuesto(edad, ingresos_mensuales):

    if edad > 16 and ingresos_mensuales >= 1000:
        resultado = "Tiene que tributar el impuesto."
    else:
        resultado = "No tiene que tributar el impuesto."
    
    return resultado

def main():
        
    edad = int(input("Ingrese su edad: "))

    ingresos_mensuales = int(input("Ingrese sus ingresos mensuales en euros: "))
    resultado = tributar_impuesto(edad, ingresos_mensuales)
    print (resultado)

if __name__ == "__main__":
    main()