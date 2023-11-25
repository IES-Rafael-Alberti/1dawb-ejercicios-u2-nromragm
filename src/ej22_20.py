from ej22_12 import pedir_frase_letra 

def encontrar_letra(frase, letra):
    resultado = ""
    for i in range(0, len(frase)):
        if frase[i] == letra:
            resultado += f"La letra esta en la posicion {i}"
            break
        else:
            resultado += f"No esta la letra en la posicion {i}\n"

    return resultado        


def main():
    frase, letra = pedir_frase_letra()
    print(encontrar_letra(frase, letra))


if __name__ == "__main__":
    main()
