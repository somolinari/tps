def capicua(cadena):
    n = len(cadena)
    for i in range(n // 2):
        if cadena[i] != cadena[n - 1 - i]:
            return False
    return True

def main ():
    cadena = input("ingresar una cadena: ")
    if capicua(cadena):
        print("La cadena es capicua")
    else:
        print("La cadena no es capicua")

if __name__ == "__main__":
    main()