import random

def matriz_aleatoria(n):
    numeros = list(range(n * n))
    random.shuffle(numeros)
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(numeros.pop())
        matriz.append(fila)
    return matriz

def main():
    n = int(input("ingrese el tamaño de la matriz N x N: "))
    matriz = matriz_aleatoria(n)

    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()
