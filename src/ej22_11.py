def pedir_palabra():
    palabra = input("Introduce una palabra: ")

    return palabra


def invertir_palabra(palabra):

    palabra_invertida = palabra[::-1]
    resultado = ""
    for letra in palabra_invertida:
        resultado += letra
    
    return resultado

def main():

    palabra = pedir_palabra()

    print(invertir_palabra(palabra))



if __name__ == "__main__":
    main()