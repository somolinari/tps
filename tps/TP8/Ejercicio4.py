def fichas(ficha1, ficha2):
    return set(ficha1) & set(ficha2) != set()

def main():
    ficha_a = (3, 4)
    ficha_b = (5, 4)
    print(fichas(ficha_a, ficha_b)) 
if __name__ == "__main__":
    main()