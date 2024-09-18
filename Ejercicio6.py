def concatenar_numeros(a, b):
   
    a_str = str(a)
    b_str = str(b)
   
    concatenado = a_str + b_str

    return int(concatenado)
def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    print(f"El número concatenado es: {concatenar_numeros(a, b)}")
if __name__ == "__main__":
    main()   