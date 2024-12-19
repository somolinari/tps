import random

def cargar_lista():
    cantidad_elementos = random.randint(10, 99)  
    lista = [random.randint(1000, 9999) for _ in range(cantidad_elementos)]
    return lista

def producto_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_valor(lista, valor):
    while valor in lista:
        lista.remove(valor)

def es_capicua(lista):
    return lista == lista[::-1]


def main ():
    lista = cargar_lista()
    print("lista cargada:", lista)
    producto = producto_lista(lista)
    print("producto de todos los elementos:", producto)
    valor_eliminar = int(input("ingresar el valor a eliminar: "))
    eliminar_valor(lista, valor_eliminar)
    print("lista con valor eliminado", lista)
    lista_capicua = [50, 17, 91, 17, 50]
    print(" es capicua?", es_capicua(lista_capicua))

if __name__ == "__main__":
    main() 