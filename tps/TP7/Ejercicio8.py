def recursiva(lista):
    if len(lista) == 0:
        return []
    min_index = 0
    for i in range(1, len(lista)):
        if lista[i] < lista[min_index]:
            min_index = i
    min_value = lista[min_index]
    lista.pop(min_index)
    return [min_value] + recursiva(lista)

def main():
    numeros = [64, 25, 12, 22, 11]
    print(f"Lista ordenada: {recursiva(numeros)}")
if __name__ == "__main__":
    main()