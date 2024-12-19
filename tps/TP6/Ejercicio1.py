def clasificar_apellidos(archivo_entrada):
    with open(archivo_entrada, 'r') as f:
        lineas = f.readlines()

    with open('ARMENIA.TXT', 'w') as armenia, \
         open('ITALIA.TXT', 'w') as italia, \
         open('ESPAÑA.TXT', 'w') as espana:

        for linea in lineas:
            apellido, nombre = linea.strip().split(', ')
            if apellido.endswith("IAN"):
                armenia.write(linea)
            elif apellido.endswith("INI"):
                italia.write(linea)
            elif apellido.endswith("EZ"):
                espana.write(linea)


def main():
    clasificar_apellidos('nombres.txt')
if __name__ == "__main__":
    main()