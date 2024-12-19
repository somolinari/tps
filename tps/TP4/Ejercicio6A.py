def extraer_subcadena(cadena, inicio, cantidad):
    return cadena[inicio:inicio + cantidad]

def main ():
    cadena = "el numero de telefono es 221505-4233"
    inicio = 25
    cantidad = 9
    print(extraer_subcadena(cadena, inicio, cantidad))

if __name__ == "__main__":
    main()
