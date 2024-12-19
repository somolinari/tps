import random

def peso_naranja():
    return random.randint(150, 350)

def procesar_naranjas(cantidad_naranjas):
    naranjas_para_jugo = 0
    naranjas_validas = 0
    peso_total = 0

    for _ in range(cantidad_naranjas):
        peso = peso_naranja()
        if 200 <= peso <= 300:
            naranjas_validas += 1
            peso_total += peso
        else:
            naranjas_para_jugo += 1

    cajones_llenos = naranjas_validas // 100
    sobrantes = naranjas_validas % 100

    camiones_necesarios = calcular_camiones(peso_total)

    return cajones_llenos, sobrantes, naranjas_para_jugo, camiones_necesarios


def calcular_camiones(peso_total):
    camiones = 0
    peso_por_camion = 500 * 1000 
    peso_minimo_ocupacion = peso_por_camion * 0.8 
    while peso_total > 0:
        if peso_total >= peso_minimo_ocupacion:
            camiones += 1
            peso_total -= peso_por_camion
        else:
            break

    return camiones

def main():
    cantidad_naranjas= int(input("Ingresa la cantidad de naranjas cosechadas: "))
    print("cantidad de camiones", {calcular_camiones}, "cantidad naranjas",cantidad_naranjas)
if __name__ == "__main__":
    main()
