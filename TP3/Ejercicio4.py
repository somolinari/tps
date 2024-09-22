import random

def crear_matriz_fabricas(N):
    matriz = [[random.randint(0, 150) for _ in range(7)] for _ in range(N)]
    return matriz

def total_fabricado_por_fabrica(matriz):
    totales = [sum(fabrica) for fabrica in matriz]
    return totales

def fabrica_max_produccion(matriz):
    max_produccion = -1
    dia_max = -1
    fabrica_max = -1
    for i, fabrica in enumerate(matriz):
        for j, produccion in enumerate(fabrica):
            if produccion > max_produccion:
                max_produccion = produccion
                dia_max = j
                fabrica_max = i
    return fabrica_max, dia_max, max_produccion

def dia_mas_productivo(matriz):
    dias_totales = [sum(matriz[fabrica][dia] for fabrica in range(len(matriz))) for dia in range(7)]
    dia_max = dias_totales.index(max(dias_totales))
    return dia_max, dias_totales[dia_max]

def menor_fabricacion_por_fabrica(matriz):
    menores = [min(fabrica) for fabrica in matriz]
    return menores

def imprimir_matriz(matriz):
    print("matriz de produccion:")
    for i, fila in enumerate(matriz):
        print(f"Fabrica {i + 1}: {fila}")

def main():
    N = int(input("ingresar el numero de fabricas: "))

    matriz_fabricas = crear_matriz_fabricas(N)
    imprimir_matriz(matriz_fabricas)

    totales_fabricas = total_fabricado_por_fabrica(matriz_fabricas)
    for i, total in enumerate(totales_fabricas):
        print(f"Total de bicicletas fabricadas por la Fabrica {i + 1}: {total}")

    fabrica_max, dia_max, max_produccion = fabrica_max_produccion(matriz_fabricas)
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    print(f"la Fabrica {fabrica_max + 1} produjo mas en un solo día con {max_produccion} bicicletas el dia {dias_semana[dia_max]}.")

    dia_mas_prod, total_dia_prod = dia_mas_productivo(matriz_fabricas)
    print(f"el dia mas productivo fue el {dias_semana[dia_mas_prod]} con un total de {total_dia_prod} bicicletas fabricadas entre todas las fabricas.")

    menores_fabricas = menor_fabricacion_por_fabrica(matriz_fabricas)
    print(f"menor cantidad fabricada por cada fabrica: {menores_fabricas}")
if __name__ == "__main__":
    main()
