def cargar_matriz(N):
    matriz = []
    for i in range(N):
        fila = []
        for j in range(N):
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def ordenar_filas(matriz):
    for fila in matriz:
        fila.sort()
    return matriz
def intercambiar_filas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz
    
def main():
    N = int(input("Ingrese el tamaño de la matriz N x N: "))
    matriz = cargar_matriz(N)
    for fila in matriz:
        print(fila)

    matriz_ordenada = ordenar_filas(matriz)
    for fila in matriz_ordenada:
        print(fila)

    fila1 = int(input("Ingrese el número de la primera fila a intercambiar: "))
    fila2 = int(input("Ingrese el número de la segunda fila a intercambiar: "))
    matriz_intercambiada = intercambiar_filas(matriz, fila1, fila2)
    for fila in matriz_intercambiada:
        print(fila)

if __name__ == "__main__":
    main()
