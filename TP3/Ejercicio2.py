def generar_matriz_a(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        matriz[i][i] = 2*i + 1
    return matriz

def generar_matriz_b(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        matriz[i][N-i-1] = 3 * (i+1) 
    return matriz

def generar_matriz_c(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            matriz[i][j] = i + 1
    return matriz

def generar_matriz_d(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j or i + j == N - 1:
                matriz[i][j] = (i + j) % 2 + 1
    return matriz

def generar_matriz_e(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matriz[i][j] = N // (2 ** (i+j)) if (i+j) < N else 0
    return matriz

def generar_matriz_f(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    valor = 1
    for i in range(N):
        if i % 2 == 0:
            for j in range(N):
                matriz[i][j] = valor
                valor += 1
        else:
            for j in range(N-1, -1, -1):
                matriz[i][j] = valor
                valor += 1
    return matriz

def generar_matriz_g(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    valor = 1
    for i in range(N):
        for j in range(N):
            matriz[i][j] = valor
            valor += 1
    return matriz

def generar_matriz_h(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    valor = 1
    for i in range(N):
        for j in range(N):
            matriz[j][i] = valor
            valor += 1
    return matriz

def generar_matriz_i(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    for i in range(N):
        if i % 2 == 0:
            matriz[i][i] = num
        num += 1
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    N = int(input("Ingrese el tamaño de la matriz (N x N): "))
    
    print("matriz a:")
    matriz_a = generar_matriz_a(N)
    imprimir_matriz(matriz_a)
    
    print("matriz b:")
    matriz_b = generar_matriz_b(N)
    imprimir_matriz(matriz_b)
    
    print("matriz c:")
    matriz_c = generar_matriz_c(N)
    imprimir_matriz(matriz_c)
    
    print("matriz d:")
    matriz_d = generar_matriz_d(N)
    imprimir_matriz(matriz_d)
    
    print("matriz e:")
    matriz_e = generar_matriz_e(N)
    imprimir_matriz(matriz_e)
    
    print("matriz f:")
    matriz_f = generar_matriz_f(N)
    imprimir_matriz(matriz_f)
    
    print("matriz g:")
    matriz_g = generar_matriz_g(N)
    imprimir_matriz(matriz_g)
    
    print("matriz h:")
    matriz_h = generar_matriz_h(N)
    imprimir_matriz(matriz_h)
    
    print("matriz i:")
    matriz_i = generar_matriz_i(N)
    imprimir_matriz(matriz_i)
main()