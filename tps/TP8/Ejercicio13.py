def buscar_clave(diccionario, valor):
    return [clave for clave, val in diccionario.items() if val == valor]

def main():
    diccionario = {'a': 1, 'b': 2, 'c': 1}
    valor_a_buscar = 1
    claves_encontradas = buscar_clave(diccionario, valor_a_buscar)
    print(f"Claves que mapean al valor {valor_a_buscar}: {claves_encontradas}")
if __name__ == "__main__":
    main()