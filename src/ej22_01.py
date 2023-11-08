def pedir_palabra():
    palabra = input("Introduce una palabra: ")

    return palabra
    

def palabra_10_veces(palabra):
    resultado = ""
    for i in range (10):
        resultado += palabra + "\n"
    return resultado

def main():

    palabra = pedir_palabra()

    print(palabra_10_veces(palabra))



if __name__ == "__main__":
    main()