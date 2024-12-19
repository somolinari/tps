import math

def raiz_cuadrada() -> float:
    while True:
        try:
            numero = float(input("Ingrese un numero para calcular su raiz cuadrada: "))
            if numero < 0:
                raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
            return math.sqrt(numero)
        except ValueError as e:
            print(f"Error: {e}")

def main():
    raiz = raiz_cuadrada()
    print(f"La raiz cuadrada es: {raiz}")
if __name__ == "__main__":
    main()   
