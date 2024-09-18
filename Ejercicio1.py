def mayor_unico(a, b, c):
    if (a > b and a > c) and (b != c):
        return a
    elif (b > a and b > c) and (a != c):
        return b
    elif (c > a and c > b) and (a != b):
        return c
    else:
        return -1

def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))

    resultado = mayor_unico(a, b, c)
    if resultado == -1:
        print("No hay un mayor único.")
    else:
        print(f"El mayor único es: {resultado}")
if __name__ == "__main__":
    main()