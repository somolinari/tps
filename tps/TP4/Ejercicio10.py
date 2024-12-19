def reemplazar_palabras(cadena, palabra_a_reemplazar, nueva_palabra):
    palabras = cadena.split()
    reemplazos = 0
    palabras_modificadas = []
    for palabra in palabras:
        if palabra.strip(str) == palabra_a_reemplazar:
            palabras_modificadas.append(nueva_palabra)
            reemplazos += 1
        else:
            palabras_modificadas.append(palabra)

    cadena_modificada = ' '.join(palabras_modificadas)
    return cadena_modificada, reemplazos
def main ():
    cadena_original = int(("ingresar una frase"))
    palabra_a_reemplazar = int(("ingresar una palabra a reemplazar"))
    nueva_palabra = int(("ingresar una nueva palabra"))
    cadena_modificada, cantidad_reemplazos = reemplazar_palabras(cadena_original, palabra_a_reemplazar, nueva_palabra)
    print("Cadena modificada:", cadena_modificada)
    print("Cantidad de reemplazos:", cantidad_reemplazos)

if __name__ == "__main__":
    main()