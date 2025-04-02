def clasificar_numeros():
    positivos = []
    negativos = []

    while True:
        try:
            numero = int(input("Ingresa un numero entero (0 para terminar): "))
            if numero == 0:
                break
            elif numero > 0:
                positivos.append(numero)
            else:
                negativos.append(numero)
        except ValueError:
            print("Ingresa SOLO números enteros.")

    resultado = {
        "positivos": len(positivos),
        "negativos": len(negativos)
    }

    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    return resultado

