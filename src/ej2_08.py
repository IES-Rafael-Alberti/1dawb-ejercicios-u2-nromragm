def pedir_puntuacion():
    salir = False
    while not salir:
        puntuacion = float(input("Introduzca su puntuacion (0.0, 0.4, 0.6 o mas): "))

        if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
            salir = True
            
        else:
            print("La puntuacion introducida no es valida.")

    return puntuacion


def calcular_rendimiento(puntuacion):
    if puntuacion == 0.0:
        resultado = (f"Inaceptable, {str(2400 * puntuacion)}€")

    elif puntuacion == 0.4:
        resultado = (f"Aceptable, {str(2400 * puntuacion)}€")
    
    elif puntuacion >= 0.6:
        resultado = (f"Meritorio, {str(2400 * puntuacion)}€")

    else:
        resultado = "La puntuacion introducida no es valida."


    return resultado


def main():

    puntuacion = pedir_puntuacion()

    resultado = calcular_rendimiento(puntuacion)

    print(resultado)


if __name__ == "__main__":
    main()