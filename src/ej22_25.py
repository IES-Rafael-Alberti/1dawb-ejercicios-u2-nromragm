def pedir_frase():
    frase = input("Introduce una frase: ")

    return frase


def palabra_larga(frase):
    resultado = ""
    palabras = frase.split()
    numero_palabras = len(palabras)
    palabra_mas_larga = ""
    
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    
    resultado += f"La palabra mas larga es: {palabra_mas_larga}\nHay un total de {numero_palabras} palabras"
    
    return resultado


def main():
    frase = pedir_frase()
    print(palabra_larga(frase))


if __name__ == "__main__":
    main()
