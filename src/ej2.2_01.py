def pedir_palabra():
    palabra = input("Introduce una palabra: ")

    return palabra
    

def palabra_10_veces(palabra):
    for i in range (1, 10):
        print(palabra)


def main():

    palabra = pedir_palabra()

    palabra_10_veces(palabra)



if __name__ == "__main__":
    main()