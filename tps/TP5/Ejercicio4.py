try:
    for i in range(1, 100001):
        print(i)
except KeyboardInterrupt:
    confirmacion = input("\n¿desea detener el programa? (s/n): ")
    if confirmacion.lower() == 's':
        print("programa detenido.")
    else:
        print("continuando...")
