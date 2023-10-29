def pedir_cantidad_interes_años():

    salir = False
    while not salir:
        cantidad = int(input("Introduze una cantidad a invertir: "))
        interes = int(input("Introduze el interes anual: "))
        años = int(input("Introduze un numero de años: "))

        if cantidad > 0 and interes > 0 and años > 0:
            salir = True
        
        else:
            print("La cantidad a invertir, interes anual o numero de años introducido no es valido.")

    return cantidad, interes, años


def capital_obtenido(cantidad, interes, años):
    for años in range(1, años + 1):
        cantidad *= 1 + interes / 100

        print(f"Año {años}: Capital obtenido = {cantidad:.2f}")


    

def main():
    
    cantidad, interes, años = pedir_cantidad_interes_años()
    
    capital_obtenido(cantidad, interes, años)


if __name__ == "__main__":
    main()