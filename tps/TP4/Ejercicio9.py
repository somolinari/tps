import string
def ordenar_por_longitud(cadena):
    palabras = cadena.split()
    palabras_sin_puntuacion = [''.join([letra for letra in palabra if letra not in string.punctuation]) for palabra in palabras]
    palabras_ordenadas = [x for _, x in sorted(zip(palabras_sin_puntuacion, palabras), key=lambda par: len(par[0]))]
    return ' '.join(palabras_ordenadas)

def main():
    cadena = "Hola, ¿como estas? Estoy muy bien"
    resultado = ordenar_por_longitud(cadena)
    print(resultado)
if __name__ == "__main__":
    main()