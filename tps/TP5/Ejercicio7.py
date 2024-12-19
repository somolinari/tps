import random

def adivinar_numero():
    numero_secreto = random.randint(1, 500)
    intentos = 0

    while True:
        intento = input("adivina un numero entre 1 y 500: ")
        intentos += 1
        try:
            intento = int(intento)
            if intento < numero_secreto:
                print("El numero es mayor.")
            elif intento > numero_secreto:
                print("El numero es menor.")
            else:
                print(f"Adivinaste,el numero era {numero_secreto}. lo adivinaste en {intentos} intentos.")
                break
        except ValueError:
            print("numero invalido. Intenta de nuevo.")
            intentos += 1 
def main():
    adivinar_numero()
if __name__ == "__main__":
    main()