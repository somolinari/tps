def resto(a, b):
    if a < b:
        return a
    return resto(a - b, b)

def main ():
    a = 10
    b = 3
    print(f"El resto de {a} dividido por {b} es: {resto(a, b)}")
if __name__ == "__main__":
    main()