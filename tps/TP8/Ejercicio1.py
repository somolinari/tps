def ingresar_fecha():
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            año = int(input("Ingrese el año: "))
            if (1 <= dia <= 31) and (1 <= mes <= 12):
                if mes in [4, 6, 9, 11] and dia == 31:
                    print("Fecha invalida.")
                    continue
                if mes == 2:
                    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                        if dia > 29:
                            print("Fecha invalida.")
                            continue
                    elif dia > 28:
                        print("Fecha invalida.")
                        continue
                return (dia, mes, año)
            else:
                print("Fecha invalida.")
        except ValueError:
            print("intente de nuevo.")

def sumar_dias(fecha, n):
    dia, mes, año = fecha
    dia += n
    while dia > 31:
        if mes in [4, 6, 9, 11] and dia > 30:
            dia -= 30
            mes += 1
        elif mes == 2:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                if dia > 29:
                    dia -= 29
                    mes += 1
            else:
                if dia > 28:
                    dia -= 28
                    mes += 1
        else:
            dia -= 31
            mes += 1
    if mes > 12:
        mes -= 12
        año += 1
    return (dia, mes, año)

def ingresar_horario():
    while True:
        try:
            horas = int(input("ingrese las horas: "))
            minutos = int(input("Ingrese los minutos: "))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                return (horas, minutos)
            else:
                print("Horario invalido.")
        except ValueError:
            print("intente de nuevo.")

def diferencia_horarios(h1, h2):
    h1_horas, h1_minutos = h1
    h2_horas, h2_minutos = h2
    total_h1 = h1_horas * 60 + h1_minutos
    total_h2 = h2_horas * 60 + h2_minutos
    if total_h1 < total_h2:
        total_h1 += 24 * 60
    diferencia = total_h1 - total_h2
    horas_dif = diferencia // 60
    minutos_dif = diferencia % 60
    return (horas_dif, minutos_dif)

def main():
    fecha = ingresar_fecha()
    n = int(input("ingresar la cantidad de dias  "))
    nueva_fecha = sumar_dias(fecha, n)
    print(f"nueva fecha: {nueva_fecha}")

    horario1 = ingresar_horario()
    horario2 = ingresar_horario()
    diferencia = diferencia_horarios(horario1, horario2)
    print(f"Diferencia entre horarios: {diferencia[0]} horas y {diferencia[1]} minutos")
if __name__ == "__main__":
    main()