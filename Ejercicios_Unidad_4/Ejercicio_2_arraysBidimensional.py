#Una matriz es un arreglo de arreglos.
#matriz [fila][columna]

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(f"Elemento en fila 0, columna 2: {matriz[0][2]}") #3
print(f"Elmento en fila 2, columna 0: {matriz[2][0]}") #7

#Recorrer la matriz completa con doble for
print("\nMatriz Completa: ")
for fila in range(len(matriz)):
    for columna in range (len(matriz[fila])):
        print(f"{matriz[fila][columna]:3}", end = " ")
print()

#Suma todos los elementos:
total = 0
for fila in matriz:
    for elemento in fila:
        total += elemento
print(f"\nSuma de todos los elementos: {total}")