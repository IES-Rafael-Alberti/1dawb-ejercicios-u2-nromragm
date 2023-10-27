def determinar_tipo_impositivo(renta):

    if renta <= 10000:
        timpo_impositivo = "5%"
    elif 10000 <= renta < 20000:
        timpo_impositivo = "15%"
    elif 20000 <= renta < 35000:
        timpo_impositivo = "20%"
    elif 35000 <= renta < 60000:
        timpo_impositivo = "30%"
    else:
        timpo_impositivo  = "45%"

    return timpo_impositivo

def main():
    renta = int(input("Ingresa su renta anual: "))
    tipo_impositivo = determinar_tipo_impositivo(renta)

    print(f"Su tipo impositivo es de {tipo_impositivo}")

if __name__ == "__main__":
    main()