def eliminar_comentarios(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        lineas = f.readlines()

    with open(archivo_salida, 'w') as salida:
        for linea in lineas:
            if '#' in linea:
                parte_comentario = linea.split('#', 1)
                linea = parte_comentario[0]
            salida.write(linea)

def main ():
    eliminar_comentarios('codigo.py', 'codigo_sin_comentarios.py')
if __name__ == "__main__":
    main()