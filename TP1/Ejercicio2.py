def es_fecha_valida(dia, mes, año):
    if mes < 1 or mes > 12 or dia < 1:
        return False
    
    dias_por_mes = [31, 29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia > dias_por_mes[mes - 1]:
        return False
    
    return True

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if es_fecha_valida(dia, mes, año):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
if __name__ == "__main__":
    main()    