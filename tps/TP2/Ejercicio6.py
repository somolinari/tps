def normalizar(lista):
    total = sum(lista)
    return [x / total for x in lista]
def main():
    lista= [1, 1, 2]
    print("Lista normalizada:", normalizar(lista))
if __name__ == "__main__":
    main() 
    