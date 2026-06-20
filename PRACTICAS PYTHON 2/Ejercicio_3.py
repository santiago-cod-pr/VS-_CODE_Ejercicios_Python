#CICLO FOR// Repite un bloque para cada elemento de una secuenci. Se usa cuando sabes de antemano cuantas veces repetir o cuando quieres recorrer los elementos de una lista, rango o cadena.

# Ejercicio: Variante de range ()
# range(fin) - empieza en 0, termina antes del fin.

print("range (5)")
for i in range (5):
    print(i, end=" ") #0 1 2 3 4 = inicia desde el numero (0)
print(" ")


# Range(inicio, fin) - desde inicio hasta fin.

print("range(1,6):")
for i in range(1, 6):
    print(i, end=" ") #12345
print(" ")

#range(inicio, fin, paso) - paso personalizado

print("Pares del 0 al 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print(" ")


# Cuenta regresiva con paso negativo:

print("Cuenta regresiva")
for i in range(5, 0, -1):
    print(i, end=" ")
print("! Despegue")


#Tu turno: Escribe un for que imprima solo los múltiplos de 3 entre 3 y 30 usando range() con los argumentos correctos. No uses if dentro del for para filtrar — usa el paso de range().

print("INCREMENTO MULTIPLOS DE 3")
for i in range(3, 31, 3):
    print(i, end=" ")
print("")


# Ejercicio - for recorriendo una lista: Promedio y conteo.
#El for no solo funciona con numeros. Puede recorrer cualquier y acumular resultados.

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]

print("calificaciones del grupo:")
for calificacion in calificaciones:
    print(f"{calificacion:.1f}")
 
total = 0
aprobados = 0
# turno de crear las variables para calificaciones alta y mas baja
max_cal = calificaciones[0]
min_cal = calificaciones[0]

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:             #Turno: encuentra e imprime la calificación más alta y la más baja. Necesitarás dos variables que guarden el máximo y el mínimo mientras recorres la lista.
        aprobados = aprobados + 1
    if calificacion > max_cal:
        max_cal = calificacion
    if calificacion < min_cal:
        min_cal = calificacion

promedio = total / len(calificaciones)
reprobados = len(calificaciones) - aprobados

print (f"\nPromedio del grupo: {promedio:.2f}")
print (f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Calificación más alta: {max_cal}")
print(f"Calificación más baja: {min_cal}")




#------------------------------------------------------------------------------------------------
#Ejercicio: for con enumerate(): indice y valor juntos
# enumerate() te da la posicion y el valor en cada iteracion. Muy util para reportes numerados.

alumnos = ["Iran", "Povedano", "Susana", "Candy", "Richard", "Itzayana", "Santiago"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 9.0]

#encabezados de la tabla:
print(f"{"N.o." :<5} {'Alumno':<12} {'Nota':>6} {'Estado':<10}")
print("-" *37)

for i, alumno in enumerate(alumnos):
    nota = notas [i]
    estado = "Aprobado" if nota >= 7.0 else "Reprobado"
    print(f"{i+1:<5} {alumno:<12} {nota:>6.1f} {estado:>10}")



    #Turno: Agrega al ejercicio un resumen al final del reporte: promedio del grupo y cantidad de aprobados, calculados dentro del mismo for que genera el reporte.

