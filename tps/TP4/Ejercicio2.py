def centrar(cadena, ancho_pantalla=80):
    espacios_izq = (ancho_pantalla - len(cadena)) // 2
    print(" " * espacios_izq + cadena)

def main():
    cadena = input("Ingrese una cadena: ")
    centrar(cadena)
if __name__ == "__main__":
    main()
