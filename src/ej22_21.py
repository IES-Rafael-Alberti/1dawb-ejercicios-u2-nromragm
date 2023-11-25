def pedir_monto():
    monto = int(input("Introduce el monto de la compra: "))

    return monto


def main():
    total = 0
    monto = pedir_monto()

    while monto != 0:
        if monto < 0:
            print("ERROR el monto debe ser positivo")
        elif monto > 0:  
            total += monto
        monto = pedir_monto()

    if total > 1000:
        total -= total * 0.1
    
    print(f"El total a pagar es de {total}€")


if __name__ == "__main__":
    main()