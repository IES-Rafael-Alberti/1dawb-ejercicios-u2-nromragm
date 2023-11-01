def pedir_frase_letra():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    return frase, letra


def veces_letra_enfrase(frase, letra):
    veces = frase.count(letra)

    resultado = print(f"La letra {letra} aparece {veces} veces en la frase.")
    
    return resultado

def main():

    frase, letra = pedir_frase_letra()

    veces_letra_enfrase(frase, letra)


if __name__ == "__main__":
    main()