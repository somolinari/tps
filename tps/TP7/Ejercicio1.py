def contar(n):
    if n < 0:
        n = -n 
    if n == 0:
        return 0
    return 1 + contar(n // 10)

def main ():
    numero = 12345
    print(f"La cantidad de digitos en {numero} es: {contar(numero)}")
if __name__ == "__main__":
    main()
