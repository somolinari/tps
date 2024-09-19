def total_gastado(Cant_viajes,total):
    
    if Cant_viajes <= 20:
        tarifa = 10
    elif 21 <= Cant_viajes <= 30:
        tarifa = 10 * 0.8
    elif 31 <= Cant_viajes <= 40:
        tarifa = 10 * 0.7
    else:
        tarifa = 10 * 0.6
    
    total=Cant_viajes*tarifa

    return total

def main():
    Cant_viajes = int(input("ingresar la cantidad de viajes: ")) 
    total=0 
    viajes= total_gastado(Cant_viajes,total)
    print("el total gastado es:",viajes)
if __name__ == "__main__":
    main() 