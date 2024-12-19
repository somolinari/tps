palos = ["Oro", "Copa", "Espada", "Basto"]
valores = [str(i) for i in range(1, 13)]  
baraja = [f"{valor} {palo}" for palo in palos for valor in valores]
for naipe in baraja:
    print(naipe)