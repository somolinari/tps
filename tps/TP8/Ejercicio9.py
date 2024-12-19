def tablas(n):
    return {i: n * i for i in range(1, 13)}

def main():
    n = int(input("Ingrese un numero entero: "))
    tabla = tablas(n)
    for i in range(1, 13):
        print(f"{n} x {i} = {tabla[i]}")
if __name__ == "__main__":
    main()