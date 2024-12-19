def fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12 or dia < 1:
        return False
    
    meses = [31, 29 if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia > meses[mes - 1]:
        return False
    
    return True

def main():
    dia = int(input("ingresar el dia: "))
    mes = int(input("ingresar el mes: "))
    anio = int(input("ingresar el año: "))

    if fecha_valida(dia, mes, anio):
        print("fecha valida")
    else:
        print("fecha no valida.")
if __name__ == "__main__":
    main()    