# Realizado por Santiago Martinez Caamal | TI21
# STRUCTURED PROGRAMMING - 21 JUNE 2026

#Constantes:
CALIFICACION_MIN_APROB = 6.0
NUMERO_ESTUDIANTES = 15

print("=====================================================")
print("======  Sistema de Registro de Calificaciones  ======")
print("=====================================================")

#Variables de Listas Vacias
nombres = []         #   guarda los nombres de los estudiantes / se rellena con el metodo .append
calificaciones = []  #   guarda las calificaciones de los estudiantes / se rellena con el metodo .append



# Entrada de los nombres de alumnos con el rango de la constante (15 alumnos)
for i in range(NUMERO_ESTUDIANTES):
    print(f"\n Estudiante: {i + 1}")
    nombre = input("Ingrese Nombre del Alumno: ")

# INGRESO DE CALIFICACION Y QUE SE ENCUENTRE DENTRO DEL RANGO DE 0 A 10:
    while True:     
        try:                                                                          #bloque try-except para manejar errores de entrada, asegurando que se ingresará un número válido para la calificación.
            calificacion = float(input("Ingrese la Calificacion del Alumno: "))
            if 0.0 <= calificacion <= 10.0:
                break
            else:
                print("/// ERROR Ingrese la calificacion dentro del rango de 0 a 10 ///")
        except:
            print("!!! INGRESE UN NUMERO VALIDO !!!")
            
    nombres.append(nombre)                      # .append, para guardar los nombres en la variable del ciclo For
    calificaciones.append(calificacion)         # .append, para guardar las calificaciones en la variable que esta dentro del while.



# / Bloque para mostar Resumen del registro de los nombres, calificaciones, estado y letra de cada alumno. /

#   Interfaz y encabezados del programa:
print("\n========================================================")
print ("==========    REGISTRO DE CALIFICACIONES     ==========")
print("========================================================")

print (f"{'N.o.' :<5} {'Alumno' :<20} {'Calificacion' :<15} {"Estado" :<13} {"Letra" :<10}")
print("-" * 70)


#  ////  CALCULOS Y CONDICIONES DEL PROGRAMA: /////

for i, nombre in enumerate(nombres):                        
    calificacion = calificaciones[i]
    estado = "Aprobado" if calificacion >= CALIFICACION_MIN_APROB else "Reprobado"
    
    if calificacion >= 9:
        letra = "A"
    elif calificacion >= 8 and calificacion <= 8.9: 
        letra = "B"
    elif calificacion >= 7 and calificacion <= 7.9:
        letra = "C"
    elif calificacion >= 6 and calificacion <= 6.9:
        letra = "D"
    else:
        letra = "F"

    print(f"{i + 1:<5} {nombre:<20} {calificacion:<15.1f} {estado:<13} {letra:<10}")


print("-"* 70)
    
# Bloque para obtener el promedio, el numero de aprobados, reprobados, calificacion mas alta y mas baja.

TOTAL = 0 
APROBADOS = 0   

# Variables con los nombres para la Calificacion mas alta y mas baja
max_cal = calificaciones[0]
min_cal = calificaciones[0]

max_cal_nombre = nombres[0]
min_cal_nombre = nombres[0]


for i, calificacion in enumerate(calificaciones):
    TOTAL =  TOTAL + calificacion               #Suma acumulada de las calificaciones para obtener el promedio al final del ciclo.
    if calificacion >= CALIFICACION_MIN_APROB:  #Si la calificacion es mayor o igual a 6, se considera aprobada y se suma 1 al contador de aprobados.
        APROBADOS += 1
    if calificacion > max_cal:  #Si la calificacion actual es mayor que la calificacion maxima registrada, se actualiza el valor de max_cal con la nueva calificacion.
        max_cal = calificacion
        max_cal_nombre = nombres[i]

    if calificacion < min_cal:  #Si la calificacion actual es menor que la calificacion minima registrada, se actualiza el valor de min_cal con la nueva calificacion.
        min_cal = calificacion
        min_cal_nombre = nombres[i]

promedio = TOTAL / len(calificaciones)                      # Calculo para saber el promedio del grupo
reprobados = len(calificaciones) - APROBADOS                # Calculos para saber la cantidad de alumnos reprobados
Porcentaje_aprob = (APROBADOS / len(calificaciones)) * 100  # Calculos para saber el porcentaje de aprobacion


#   //// RESUMEN DE LOS NOMBRES Y CALIFICACIONES INGRESADAS (Representacion / salida de los calculos): /////

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {APROBADOS} |  Reprobados: {reprobados}")
print("-" * 70)

print(f"Mejor Calificación: {max_cal_nombre} con: {max_cal}")
print(f"Peor Calificación: {min_cal_nombre} con: {min_cal}")
print(f"Porcentaje de aprobacion del grupo: {Porcentaje_aprob:.1f}%")