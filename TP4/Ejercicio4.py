def romano(n):
    valores_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    resultado = ""
    
    for valor, simbolo in valores_romanos:
        while n >= valor:
            resultado += simbolo
            n -= valor
    
    return resultado
def main():
    numero = int(input("Ingrese un número entre 0 y 3999: "))
    print(f"El número romano es: {romano(numero)}")
if __name__ == "__main__":
    main()