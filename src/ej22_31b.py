def pedirEdad(msj: str):
    error = True
    while error:
        try:
            edad = int(input(msj))
            error = False
        
        except:
            print("Error edad no valida")
        
    return edad

def años_cumplidos(edad: int) -> str:
    serie = ""
    for i in range(1, edad + 1):
        serie += str(i) + " "

    return serie

def main():

    edad = pedirEdad("Introduzca su edad: ")

    print(f"Años que has cumplido: {años_cumplidos(edad)}")
    



if __name__ == "__main__":
    main()