def cuadrados(N):
    return [i**2 for i in range(1, N+1)]


def main ():
    N= int(input("ingresar el valor de N: "))
    lista_cuadrados = cuadrados(N)
    print("ultimos 10 valores de la lista:",lista_cuadrados[-10:])

if __name__ == "__main__":
    main() 
