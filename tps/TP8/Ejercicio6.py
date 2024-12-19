def eliminar_repe(frase):
    palabras = frase.split()
    conjunto_palabras = set(palabras)
    return sorted(conjunto_palabras, key=len)

def main():
    frase = "hola mundo hola python"
    print(eliminar_repe(frase))
if __name__ == "__main__":
    main()