def pedir_palabra():
    palabra = input("Introduce una palabra: ")

    return palabra


def invertir_palabra(palabra):

    palabra_invertida = palabra[::-1]

    for letra in palabra_invertida:
        print(letra)
    
    return letra

def main():

    palabra = pedir_palabra()

    invertir_palabra(palabra)



if __name__ == "__main__":
    main()