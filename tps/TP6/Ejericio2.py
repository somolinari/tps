def dividir_archivo(archivo_entrada, tamaño_maximo):
    try:
        with open(archivo_entrada, 'r') as f:
            parte_num = 1
            parte_actual = []
            tamaño_actual = 0

            for linea in f:
                tamaño_linea = len(linea)
                if tamaño_actual + tamaño_linea > tamaño_maximo:
                    with open(f"{archivo_entrada}_parte{parte_num}.txt", 'w') as parte:
                        parte.writelines(parte_actual)
                    parte_num += 1
                    parte_actual = []
                    tamaño_actual = 0

                parte_actual.append(linea)
                tamaño_actual += tamaño_linea

            if parte_actual:
                with open(f"{archivo_entrada}_parte{parte_num}.txt", 'w') as parte:
                    parte.writelines(parte_actual)

    except Exception as e:
        print(f"Error: {e}")

dividir_archivo('archivo.txt', 1000)