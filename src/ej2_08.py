def calcular_rendimiento(puntuacion):
    if puntuacion == 0.0:
        rendimiento = "Inaceptable"

    elif puntuacion == 0.4:
        rendimiento = "Aceptable"

    else:
        rendimiento = "Meritorio"

    cantidad_dinero = 2400 * puntuacion

    return rendimiento, cantidad_dinero


def main():

    puntuacion = float(input("Ingresa la puntuacion del empleado (0.0, 0.4, 0.6 o mas): "))

    if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
        rendimiento2, cantidad_dinero2 = calcular_rendimiento(puntuacion)

        print(f"Nivel de rendimiento: {rendimiento2}\nCantidad de dinero recibida: {cantidad_dinero2}€")


    else:
        print("La puntuación ingresada no es valida")


if __name__ == "__main__":
    main()