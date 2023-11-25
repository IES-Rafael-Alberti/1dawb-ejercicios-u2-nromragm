def comenzar_programa():
    resultado = "El programa ha comenzado."

    return resultado

def imprimir_listado():
    resultado = "Lista de elementos: Agua, Pan"

    return resultado


def main():
    salir = False
    while not salir:
        print("Menu:")
        print("1- Comenzar programa")
        print("2- Imprimir listado")
        print("3- Finalizar programa")
        
        opcion = input("Seleccione una opcion (1, 2 o 3): ")
        
        if opcion == "1":
            print(comenzar_programa())
        elif opcion == "2":
            print(imprimir_listado())
        elif opcion == "3":
            print("Programa finalizado.")
            salir = True
        else:
            print("Opcion incorrecta. Seleccione una opcion valida (1, 2 o 3).")

if __name__ == "__main__":
    main()
