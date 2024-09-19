def eliminar(lista_original, lista_eliminar):
    for valor in lista_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

def main():
    lista_original = [1, 2, 3, 4, 5, 6]
    lista_eliminar = [2, 4, 6]
    eliminar(lista_original, lista_eliminar)
    print("lista despues de eliminar", lista_original)
if __name__ == "__main__":
    main() 

