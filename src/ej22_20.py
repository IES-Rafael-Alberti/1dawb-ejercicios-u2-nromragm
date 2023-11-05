from ej22_12 import pedir_frase_letra 

def encontrar_letra(frase, letra):
    for i in range(0, len(frase)):
        if frase[i] == letra:
            print(f"La letra esta en la posicion {i}")
            break
        else:
            print(f"No esta la letra en la posicion {i}")


def main():
    frase, letra = pedir_frase_letra()
    encontrar_letra(frase, letra)


if __name__ == "__main__":
    main()
