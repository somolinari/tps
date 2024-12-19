def fecha_extendido(fecha):
    dias = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    dia, mes, año = fecha
    if año < 100:
        año += 2000 if año >= 30 else 1900
    return f"{dias[dia]} de {meses[mes - 1]} de {año}"

def main():
    fecha = (12, 10, 30) 
    print(fecha_extendido(fecha))

    fecha2 = (25, 12, 31) 
    print(fecha_extendido(fecha2))
if __name__ == "__main__":
    main()