def concatenar_numeros(num1, num2):
   
    num1_str = str(num1)
    num2_str = str(num2)
   
    concatenado = num1_str + num2_str

    return int(concatenado)
def main():
    num1 = int(input("ingresar el primer numero: "))
    num2 = int(input("ingresar el segundo numero: "))
    resultado=concatenar_numeros(num1,num2)

    print("el numero concatenado es:",resultado)
if __name__ == "__main__":
    main()   