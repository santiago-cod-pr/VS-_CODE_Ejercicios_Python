# Realizado por Santiago Martinez Caamal | TI21

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

    # INGRESO DE LOS DATOS DE CALIFICACION Y QUE SE ENCUENTREN DENTRO DEL RANGO DE 0 A 10:
    while True:     
        try:                                                                          #bloque try-except para manejar errores de entrada, asegurando que se ingresara un número válido para la calificación.
            calificacion = float(input("Ingrese la Calificacion del Alumno: "))
            if 0.0 <= calificacion <= 10.0:
                break
            else:
                print("/// ERROR Ingrese la calificacion dentro del rango de 0 a 10 ///")
        except:
            print("!!! INGRESE UN NUMERO VALIDO !!!")
            
    nombres.append(nombre)                      # .append, para guardar los nombres en la variable del ciclo For
    calificaciones.append(calificacion)         # .append, para guardar las calificaciones en la variable que esta dentro del while.


# Bloque para mostar Resumen del registro de los nombres, calificaciones, estado y letra de cada alumno.
print("\n========================================================")
print ("==========    REGISTRO DE CALIFICACIONES     ==========")
print("========================================================")

print (f"{'N.o.' :<5} {'Alumno' :<20} {'Calificacion' :<15} {"Estado" :<13} {"Letra" :<10}")
print("-" * 70)


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

# Variables: Calificacion mas alta y mas baja
max_cal = calificaciones[0]
min_cal = calificaciones[0]

for calificacion in calificaciones:
    TOTAL =  TOTAL + calificacion               #Suma acumulada de las calificaciones para obtener el promedio al final del ciclo.
    if calificacion >= CALIFICACION_MIN_APROB:  #Si la calificacion es mayor o igual a 6, se considera aprobada y se suma 1 al contador de aprobados.
        APROBADOS += 1
    if calificacion > max_cal:
        max_cal = calificacion
    if calificacion < min_cal:
        min_cal = calificacion

promedio = TOTAL / len(calificaciones)
reprobados = len(calificaciones) - APROBADOS

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {APROBADOS} |  Reprobados: {reprobados}")
print(f"Calificación más alta: {max_cal}")
print(f"Calificación más baja: {min_cal}")