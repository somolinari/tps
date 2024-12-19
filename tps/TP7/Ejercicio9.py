def imprimir_matriz(matriz, fila=0, col=0):
    if fila < len(matriz):
        if col < len(matriz[fila]):
            print(matriz[fila][col], end=' ')
            imprimir_matriz(matriz, fila, col + 1)
        else:
            print()
            imprimir_matriz(matriz, fila + 1, 0)

def main ():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8,  9]]
    imprimir_matriz(matriz)
if __name__ == "__main__":
    main()