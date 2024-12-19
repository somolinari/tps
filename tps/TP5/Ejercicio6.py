def buscar_lista():
    lista = []
    while True:
        numero = int(input("Ingrese un numero entero o -1 para terminar: "))
        if numero == -1:
            break
        lista.append(numero)

    errores = 0
    while errores < 3:
        try:
            valor_buscar = int(input("Ingrese un numero para buscar su posicion: "))
            posicion = lista.index(valor_buscar)
            print(f"El numero {valor_buscar} esta en la posicion: {posicion}")
        except ValueError:
            errores += 1
            print(" El numero no esta en la lista.")
            if errores == 3:
                print("Se alcanzo el limite de errores. Saliendo...")
                break

def main():
    buscar_lista()
if __name__ == "__main__":
    main()