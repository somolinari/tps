def sumar_cadenas(cadena1, cadena2) -> float:
    try:
        num1 = float(cadena1)
        num2 = float(cadena2)
        return num1 + num2
    except ValueError:
        return -1

def main ():
    resultado = sumar_cadenas("3.5", "2.5")
    if resultado != -1:
        print(f"La suma es: {resultado}")
    else:
        print("una de las cadenas no contiene un numero valido.")
if __name__ == "__main__":
    main()