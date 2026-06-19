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


# Ingreso de los nombres de los alumnos con el rango de la constante (15 alumnos)
for i in range(NUMERO_ESTUDIANTES):
    print(f"\n Estudiante: {i + 1}")
    nombre = input("Ingrese Nombre del Alumno: ")

    # INGRESO DE LOS DATOS DE: CALIFICACION Y QUE SE ENCUENTREN DENTRO DEL RANGO DE 0 A 10:
    while True:
        try:
            calificacion = float(input("Ingrese la Calificacion del Alumno: "))
            if 0.0 <= calificacion <= 10.0:
                break
            else:
                print("/// ERROR Ingrese la calificacion dentro del rango de 0 a 10 ///")
        except:
            print("!!! INGRESE UN NUMERO VALIDO !!!")



nombres.append(nombre)                      # .append, para guardar los nombres en la variable del ciclo For
calificaciones.append(calificacion)         # .append, para guardar las calificaciones en la variable que esta dentro del while.






