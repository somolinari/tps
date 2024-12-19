import random 
def generar_lista_numeros(N):
    return [random.randint(1, 100) for _ in range(N)]

def tiene_repetidos(lista):
    return len(lista) != len(set(lista))

def elementos_unicos(lista):
    return list(set(lista))

def main():
    N = int(input("Ingresa el valor de N: "))
    lista_numeros = generar_lista_numeros(N)
    print("lista generada:", lista_numeros)
    print("lista conn elementos unicos:", elementos_unicos(lista_numeros))
    print("tiene elementos repetidos?", tiene_repetidos(lista_numeros))

if __name__ == "__main__":
    main() 