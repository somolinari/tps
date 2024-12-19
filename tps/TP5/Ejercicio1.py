def numero_natural() -> int:
    while True:
        try:
            numero = int(input("Ingrese un numero natural: "))
            if numero <= 0:
                raise ValueError("El numero debe ser mayor que 0.")
            return numero
        except ValueError as e:
            print(f"Error: {e}")

def main ():
    numero = numero_natural()
    print(f"Numero ingresado correctamente: {numero}")

if __name__ == "__main__":
    main()