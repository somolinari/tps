def archivo_fijo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        with open(archivo_salida, 'w') as salida:
            for linea in f:
                campos = [linea[i:i+10].strip() for i in range(0, len(linea), 10)]
                salida.write(','.join(campos) + '\n')

def archivo_variable(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        with open(archivo_salida, 'w') as salida:
            for linea in f:
                i = 0
                while i < len(linea):
                    longitud = int(linea[i:i+2])
                    i += 2
                    campo = linea[i:i+longitud].strip()
                    salida.write(campo + ',')
                    i += longitud
                salida.write('\n')

def main():
    archivo_fijo('empleados_fijo.txt', 'empleados_fijo.csv')
    archivo_variable('empleados_variable.txt', 'empleados_variable.csv')
if __name__ == "__main__":
    main()