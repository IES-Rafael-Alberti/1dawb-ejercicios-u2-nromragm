def determinar_grupo(nombre, sexo):

    if sexo == "M" and nombre < "M":
        grupo = "A"
    elif sexo == "H" and nombre > "N":
        grupo = "A"
    else:
        grupo = "B"

    return grupo


def main():

    nombre = input("Ingresa tu nombre: ")
    sexo = input("Ingresa tu sexo (M para mujer, H para hombre): ")
    grupo = f"Perteneces al grupo: {determinar_grupo(nombre, sexo)}"

    print(grupo)


if __name__ == "__main__":
    main()