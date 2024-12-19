def mcd(x, y):
    if x == y:
        return x
    elif x > y:
        return mcd(x - y, y)
    else:
        return mcd(x, y - x)

def mcd_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return mcd(lista[0], mcd_lista(lista[1:]))

def main():
    numeros= [48, 64, 32]
    print(f"el MCD {numeros} es: {mcd_lista(numeros)}")
if __name__ == "__main__":
    main()