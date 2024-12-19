def suma_matriz(matriz):
    if not matriz:
        return 0
    return suma_fila(matriz[0]) + suma_matriz(matriz[1:])

def suma_fila(fila):
    if not fila:
        return 0
    return fila[0] + suma_fila(fila[1:])

def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"la suma de todos los elementos es: {suma_matriz(matriz)}")
if __name__ == "__main__":
    main()