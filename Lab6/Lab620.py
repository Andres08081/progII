matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Generación automática (matriz identidad)
n = 3
identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("Matriz manual:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t")
    print()