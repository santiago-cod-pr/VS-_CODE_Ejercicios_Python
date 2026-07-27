#Cuando ejcutamos el programa sin "Archivos" se carga en la RAM, y se elimina al cerrarlo.

#La forma recomendada de trabajar con archivos em python es usando el bloque with.
#Su ventaja principal es que cierra el archivo automaticamente al salir del bloque, incluso si
#ocurre un error. No hay que llamar al archivo.close() manualmente.

#Escribir y leer archivo de texto
with open("notas.txt", "w", encoding= "utf-8") as archivo:
    archivo.write("Povedano: 9.5\n")
    archivo.write("Santiago: 8.9\n")
    archivo.write("Gissel: 8.4\n")
    archivo.write("Alexandro: 7.3\n")
    archivo.write("Sulub: 6.9")
    
print("Archivo Creado Correctamente")

# LEER - READ() lee todo el contenido de una vez
print("\n----- Contenido con read() -----")
with open("notas.txt", "r", encoding= "utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# ignora líneas vacías

#-------------------------------------------------------------------------------------------------------

#HACERLO EN EL ARCHIVO ejercic103_archivos

# LEER LÍNEA POR LÍNEA - readlines() regresa una lista
print(" --- Contenido con readlines() --- ")
with open("notas.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# strip() elimina el \n del final

# - Ejercicio 7: Procesar contenido de un archivo
# El archivo notas.txt tiene el formato "Nombre: Calificación"

def cargar_calificaciones(nombre_archivo):
    """
    Lee el archivo y regresa una lista de diccionarios.
    Cada diccionario tiene 'nombre' y 'nota'.
    """
    alumnos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split(": ")
                nombre = partes[0]
                nota = float(partes[1])
                alumnos.append({"nombre": nombre, "nota": nota})
    return alumnos


def mostrar_reporte(alumnos):
    """Imprime el reporte de calificaciones."""
    print(f"\n{'Nombre':<15} {'Nota':>6} {'Estado':<10}")
    print("-" * 35)
    total = 0
    for alumno in alumnos:
        estado = "Aprobado" if alumno["nota"] >= 6.0 else "Reprobado"
        print(f"{alumno['nombre']:<15} {alumno['nota']:>6.1f} {estado:<10}")
        total += alumno["nota"]
    print("-" * 35)
    print(f"Promedio del grupo: {total/len(alumnos):.2f}")

alumnos = cargar_calificaciones("notas.txt")
mostrar_reporte(alumnos)

# --- Ejercicio 8: Ciclo cargar -> modificar -> guardar -----------
def guardar_calificaciones(nombre_archivo, alumnos):
    """Guarda la lista de alumnos en el archivo."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for alumno in alumnos:
            linea = f"{alumno['nombre']}: {alumno['nota']}\n"
            archivo.write(linea)
    print(f"Datos guardados en {nombre_archivo}")

# Ciclo completo
alumnos = cargar_calificaciones("notas.txt")

# Modificar en memoria: agregar un alumno nuevo
alumnos.append({"nombre": "Roberto", "nota": 8.0})

# Guardar de vuelta al archivo
guardar_calificaciones("notas.txt", alumnos)

# Verificar que se guardó correctamente
alumnos_verificacion = cargar_calificaciones("notas.txt")
mostrar_reporte(alumnos_verificacion)