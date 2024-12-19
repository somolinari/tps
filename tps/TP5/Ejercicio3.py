def nombre_mes(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        if numero_mes < 1 or numero_mes > 12:
            raise IndexError("Numero de mes invalido.")
        return meses[numero_mes - 1]
    except IndexError as e:
        print(f"Error: {e}")
        return ""
def main():
    mes = nombre_mes(5)
    if mes:
        print(f"el mes es: {mes}")
    else:
        print("no se pudo obtener el mes")
if __name__ == "__main__":
    main()
