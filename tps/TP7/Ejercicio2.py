def binario_a_decimal(binario):
    if binario == 0:
        return 0
    return (binario % 10) + 2 * binario_a_decimal(binario // 10)

def main():
    numero_binario = 1011
    print(f"El numero binario {numero_binario} en decimal es: {binario_a_decimal(numero_binario)}")
if __name__ == "__main__":
    main()