def rango_alturas(archivo_salida):
    with open(archivo_salida, 'w') as f:
        while True:
            deporte = input("ingrese el deporte, o 'fin' para terminar: ")
            if deporte.lower() == 'fin':
                break
            f.write(deporte + '\n')
            while True:
                altura = input(f"ingrese la altura del atleta {deporte} ,o 'fin' para terminar: ")
                if altura.lower() == 'fin':
                    break
                f.write(altura + '\n')

def promedio(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        lineas = f.readlines()

    promedios = {}
    deporte_actual = ""
    alturas = []

    for linea in lineas:
        linea = linea.strip()
        if linea.isalpha():
            if deporte_actual and alturas:
                promedio = sum(map(float, alturas)) / len(alturas)
                promedios[deporte_actual] = promedio
            deporte_actual = linea
            alturas = []
        else:
            alturas.append(float(linea))

    if deporte_actual and alturas:
        promedio = sum(map(float, alturas)) / len(alturas)
        promedios[deporte_actual] = promedio

    with open(archivo_salida, 'w') as f:
        for deporte, promedio in promedios.items():
            f.write(f"{deporte}\n{promedio}\n")

def altos(archivo_promedios):
    with open(archivo_promedios, 'r') as f:
        lineas = f.readlines()

    promedios = {}
    for i in range(0, len(lineas), 2):
        deporte = lineas[i].strip()
        promedio = float(lineas[i + 1].strip())
        promedios[deporte] = promedio

    promedio_general = sum(promedios.values()) / len(promedios)
    print("deportes con atletas que superan la altura promedio general:")
    for deporte, promedio in promedios.items():
        if promedio > promedio_general:
            print(deporte)
def main ():
    rango_alturas('atletas.txt')
    promedio('atletas.txt', 'promedios.txt')
    altos('promedios.txt')
if __name__ == "__main__":
    main()   