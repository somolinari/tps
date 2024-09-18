def total_gastado(viajes):
    if viajes <= 20:
        tarifa = 10
    elif 21 <= viajes <= 30:
        tarifa = 10 * 0.8
    elif 31 <= viajes <= 40:
        tarifa = 10 * 0.7
    else:
        tarifa = 10 * 0.6
    
    return viajes * tarifa

def main():
    viajes = int(input("Ingrese la cantidad de viajes: "))  
    print(f"El total gastado es: {total_gastado(viajes)}")
if __name__ == "__main__":
    main() 