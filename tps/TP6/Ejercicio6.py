import csv
from datetime import datetime

def registrar_huespedes(archivo_salida):
    with open(archivo_salida, 'w', newline='') as f:
        writer = csv.writer(f)
        while True:
            dni = int(input("Ingrese el DNI del cliente (-1 para terminar): "))
            if dni == -1:
                break
            apellido_nombre = input("Ingrese Apellido y Nombre: ")
            fecha_ingreso = input("Ingrese fecha de ingreso (DDMMAAAA): ")
            fecha_egreso = input("Ingrese fecha de egreso (DDMMAAAA): ")
            cantidad_ocupantes = int(input("Ingrese cantidad de ocupantes: "))
            writer.writerow([dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes])

def asignar_habitaciones(archivo_huespedes):
    with open(archivo_huespedes, 'r') as f:
        reader = csv.reader(f)
        habitaciones = {}
        for row in reader:
            dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes = row
            piso = len(habitaciones) // 6 + 1
            habitacion = len(habitaciones) % 6 + 1
            habitaciones[dni] = (apellido_nombre, piso, habitacion, fecha_ingreso, fecha_egreso, cantidad_ocupantes)

    return habitaciones

def habitaciones_ocupadas(habitaciones):
    ocupadas = {}
    for dni, datos in habitaciones.items():
        piso = datos[1]
        if piso not in ocupadas:
            ocupadas[piso] = 0
        ocupadas[piso] += 1

    piso_max_ocupado = max(ocupadas, key=ocupadas.get)
    print(f"piso con mayor cantidad de habitaciones ocupadas: {piso_max_ocupado}")

def habitaciones_vacias(habitaciones):
    total_habitaciones = 10 * 6
    ocupadas = len(habitaciones)
    print(f"total de habitaciones vacías: {total_habitaciones - ocupadas}")

def proxima_habitacion_desocupada(habitaciones, fecha_actual):
    desocupadas = []
    for dni, datos in habitaciones.items():
        fecha_egreso = datetime.strptime(datos[4], "%d%m%Y")
        if fecha_egreso > fecha_actual:
            desocupadas.append((dni, datos))

    return desocupadas
def main():
    registrar_huespedes('huespedes.csv')
    habitaciones = asignar_habitaciones('huespedes.csv')
    habitaciones_ocupadas(habitaciones)
    habitaciones_vacias(habitaciones)
    fecha_actual = datetime.strptime(input("ingresar la fecha actual: "), "%d%m%Y")
    desocupadas = proxima_habitacion_desocupada(habitaciones, fecha_actual)
    print("habitaciones que se desocupan proximamente:", desocupadas)
if __name__ == "__main__":
    main()