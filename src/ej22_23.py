def titulo_libro():
    resultado = ""
    lista = ""
    titulo = ""
    linea = 0
    while titulo != "*":
        titulo = input("Libro: ")
        if titulo == "/":
            digitos = 0
            for i in range (0, len(lista)):
                if lista[i].isnumeric():
                    digitos += 1

            print(f"Linea completa. Aparecen {digitos} dígitos númericos")
            linea += 1

        else:
            lista += titulo
    resultado += f"Fin. Se leyeron {linea} líneas completas."

    return resultado


def main():
    print(titulo_libro())
    

if __name__ == "__main__":
    main()