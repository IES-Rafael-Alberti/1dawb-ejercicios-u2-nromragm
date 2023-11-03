def pedir_palabra():
    palabra = input("Introduce una palabra: ")

    return palabra
    

def palabra_10_veces(palabra):
    for i in range (10):
        resultado = print(palabra)
        return resultado

def main():

    palabra = pedir_palabra()

    palabra_10_veces(palabra)



if __name__ == "__main__":
    main()