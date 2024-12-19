def validar_fecha(fecha):
    if len(fecha) != 8 or not fecha.isdigit():
        return False
    dia, mes, año = int(fecha[:2]), int(fecha[2:4]), int(fecha[4:])
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in {4, 6, 9, 11} and dia > 30:
        return False
    if año < 2000:
        return False

def registrar_huespedes(archivo_salida):
    with open(archivo_salida, 'w') as f:
        while True:
            dni = input("Ingrese el DNI del cliente (-1 para terminar): ")
            if dni == "-1":
                break
            apellido_nombre = input("ngrese Apellido y Nombre: ")
            fecha_ingreso = input("ingrese fecha de ingreso (DDMMAAAA): ")
            while not validar_fecha(fecha_ingreso):
                print("Fecha invalida, intente nuevamente")
                fecha_ingreso = input("ingrese fecha de ingreso (DDMMAAAA): ")
            fecha_egreso = input("ingrese fecha de egreso (DDMMAAAA): ")
            while not validar_fecha(fecha_egreso):
                print("Fecha invalida,intente nuevamente")
                fecha_egreso = input("ingrese fecha de egreso (DDMMAAAA): ")
            cantidad_ocupantes = input("ingrese cantidad de ocupantes: ")
            f.write(f"{dni},{apellido_nombre},{fecha_ingreso},{fecha_egreso},{cantidad_ocupantes}\n")

def asignar_habitaciones(archivo_huespedes):
    habitaciones = {}
    with open(archivo_huespedes, 'r') as f:
        for linea in f:
            dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes = linea.strip().split(',')
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
    print(f"Piso con mayor cantidad de habitaciones ocupadas: {piso_max_ocupado}")

def habitaciones_vacias(habitaciones):
    total_habitaciones = 10 * 6
    ocupadas = len(habitaciones)
    print(f"Total de habitaciones vacías: {total_habitaciones - ocupadas}")

def proxima_habitacion_desocupada(habitaciones, fecha_actual):
    desocupadas = []
    for dni, datos in habitaciones.items():
        fecha_egreso = datos[4]
        if fecha_egreso > fecha_actual:
            desocupadas.append((dni, datos))
    return desocupadas

def main():
    archivo_huespedes = 'huespedes.txt'
    registrar_huespedes(archivo_huespedes)
    habitaciones = asignar_habitaciones(archivo_huespedes)
    habitaciones_ocupadas(habitaciones)
    habitaciones_vacias(habitaciones)
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    while not validar_fecha(fecha_actual):
        print("Fecha inválida. Intente nuevamente.")
        fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    desocupadas = proxima_habitacion_desocupada(habitaciones, fecha_actual)
    print("Habitaciones que se desocupan próximamente:")
    for dni, datos in desocupadas:
        print(f"DNI: {dni}, Nombre: {datos[0]}, Fecha de egreso: {datos[4]}")

if __name__ == "__main__":
    main()