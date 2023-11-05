def pedir_frase():
    frase = input("Introduce una frase: ")

    return frase


def palabra_larga(frase):
    palabras = frase.split()
    numero_palabras = len(palabras)
    palabra_mas_larga = ""
    
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    
    print(f"La palabra mas larga es: {palabra_mas_larga}")
    print(f"Hay un total de {numero_palabras} palabras.")


def main():
    frase = pedir_frase()
    palabra_larga(frase)


if __name__ == "__main__":
    main()
