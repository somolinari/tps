def producto(a, b):
    if b == 0:
        return 0
    return a + producto(a, b - 1)

def main ():
    a = 5
    b = 3
    print(f"El producto de {a} y {b} es: {producto(a, b)}")
if __name__ == "__main__":
    main()