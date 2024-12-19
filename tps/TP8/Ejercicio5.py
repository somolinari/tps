def ortogonales(v1, v2):
    producto_escalar = v1[0] * v2[0] + v1[1] * v2[1]
    return producto_escalar == 0

def main():
    vector_a = (2, 3)
    vector_b = (-3, 2)
    print(ortogonales(vector_a, vector_b)) 
if __name__ == "__main__":
    main()