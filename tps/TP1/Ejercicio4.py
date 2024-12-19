def calcular_cambio(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        return "dinero recibido insuficiente"
    
    cambio = dinero_recibido - total_compra
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    resultado = {}
    
    for billete in billetes:
        cantidad = cambio // billete
        if cantidad > 0:
            resultado[billete] = cantidad
            cambio -= cantidad * billete
    
    if cambio > 0:
        return "No se puede entregar cambio"
    
    return resultado

def main():
    total_compra = int(input("ingresar el total de la compra: "))
    dinero_recibido = int(input("ingresar el dinero recibido: "))

    resultado = calcular_cambio(total_compra, dinero_recibido)
    print("el resultado es:",resultado)
if __name__ == "__main__":
    main()   