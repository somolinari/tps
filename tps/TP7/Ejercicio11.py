def minimo_matriz(matriz):
    if not matriz:
        return float('inf')
    return min(minimo_fila(matriz[0]), minimo_matriz(matriz[1:]))

def minimo_fila(fila):
    if not fila:
        return float('inf')
    return min(fila[0], minimo_fila(fila[1:]))
def main():
    matriz = [[3, 5, 1], [4, 2, 6], [7, 8, 0]]
    print(f"El minimo elemento de la matriz es: {minimo_matriz(matriz)}")
if __name__ == "__main__":
    main()