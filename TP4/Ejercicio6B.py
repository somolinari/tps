def extraer_subcadena_sin_rebanadas(cadena, inicio, cantidad):
    subcadena = ""
    for i in range(inicio, inicio + cantidad):
        subcadena += cadena[i]
    return subcadena