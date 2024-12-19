def ackerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))
def main ():
    for m in range(4):
        for n in range(8):
            print(f"A({m}, {n}) = {ackerman(m, n)}")
if __name__ == "__main__":
    main()
