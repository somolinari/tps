def contar_vocales(palabra):
    vocales = 'aeiou'
    conteo = {v: palabra.lower().count(v) for v in vocales}
    return conteo
def main():
    frase = "Hola mundo"
    for palabra in frase.split():
        print(f"{palabra}: {contar_vocales(palabra)}")
if __name__ == "__main__":
    main()