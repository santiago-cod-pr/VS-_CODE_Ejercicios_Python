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


#Ejercicio 5 - Aplicacion real de matriz: calificaciones por alumno y materia

#--- Ejercicio 5 - Matriz de calificaciones ---------------------------------
alumnos = ["Ana", "Luis", "Sofia", "Carlos"]
materias = ["Matematicas", "Python", "Redes", "S0"]

calificaciones = [
    [9.0, 8.5, 7.0, 9.5],  #Ana
    [7.5, 6.0, 8.0, 7.0],  #Luis
    [10.0, 9.5, 9.0, 8.5], #Sofia
    [5.0, 6.5, 7.5, 6.0],  #Carlos
]

#Encabezados
print(f"{'Alumno':<10}", end="")
for materia in materias:
    print(f"{materia:>14}", end="")
print(f"{'promedio':>12}")
print("-" * 70)

#Datos por alumno
for i, alumno in enumerate(alumnos):
    print(f"{alumno:<10}", end="")
    total = 0
    for cal in calificaciones[i]:
        print(f"{cal:>14.1f}", end="")
        total += cal
    promedio = total / len(materias)
    print(f"{promedio:>12.2f}")
