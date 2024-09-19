def intercalar(lista1, lista2):
    lista1[::2], lista1[1::2] = lista1, lista2[:len(lista1)]
    lista1.extend(lista2[len(lista1):])

def main ():
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    intercalar(lista1, lista2)
    print("lista intercalada:", lista1)

if __name__ == "__main__":
    main() 