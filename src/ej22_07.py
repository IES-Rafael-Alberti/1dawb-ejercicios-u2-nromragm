def tabla_de_multiplicar(numero):
    for i in range(1, 10 + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def mostrar_tabla():
    for i in range(1, 10 + 1):
        print(f"Tabla del {i}:")
        tabla_de_multiplicar(i)
        print("")

def main():
    print("Tabla de multiplicar del 1 al 10:")
    mostrar_tabla()

if __name__ == "__main__":
    main()