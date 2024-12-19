def gestionar_conjunto():
    conjunto = set(range(10))
    while True:
        try:
            valor = int(input("ingresar un numero entre 0 y 9 para eliminar -1 para salir: "))
            if valor == -1:
                break
            conjunto.remove(valor)
            print(f"conjunto actual: {conjunto}")
        except KeyError:
            print("El numero no esta en el conjunto.")
        except ValueError:
            print("intente de nuevo.")
def main ():
    gestionar_conjunto()
if __name__ == "__main__":
    main()