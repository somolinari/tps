def mayor(num1 , num2, num3):
    if (num1 > num2 and num1 > num3) and (num2 != num3):
        return num1
    elif (num2 > num1 and num2 > num3) and (num1 != num3):
        return num2
    elif (num3 > num1 and num3 > num2) and (num1 != num2):
        return num3
    else:
        return -1

def main():
    num1 = int(input("ingresarvel 1er numero: "))
    num2 = int(input("Ingresar el 2do numero: "))
    num3 = int(input("Ingresar el 3er numero: "))

    resultado = mayor(num1, num2, num3)
    if resultado == -1:
        print("no existe un maximo")
    else:
        print("el maximo es: ",resultado)
if __name__ == "__main__":
    main()