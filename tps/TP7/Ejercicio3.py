def suma_naturales(n):
    if n == 0:
        return 0
    return n + suma_naturales(n - 1)

def main():
    n = 5
    print(f"la suma de los primeros {n} numeros naturales es: {suma_naturales(n)}")
if __name__ == "__main__":
    main()