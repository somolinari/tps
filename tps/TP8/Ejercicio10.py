def eliminar_claves(diccionario, claves):
    eliminadas = 0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            eliminadas += 1
    return diccionario, eliminadas

def main():
    diccionario = {'a': 1, 'b': 2, 'c': 3}
    claves_eliminar = ['a', 'c']
    nuevo_diccionario, cantidad_eliminadas = eliminar_claves(diccionario, claves_eliminar)
    print(nuevo_diccionario, cantidad_eliminadas)
if __name__ == "__main__":
    main()