n = int(input("Ingresa el orden N (numero par): "))

if n % 2 != 0:
    print("Error: N debe ser un numero par.")
else:
    
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)

    print(f"\nMatriz identidad :")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="  ")
        print()