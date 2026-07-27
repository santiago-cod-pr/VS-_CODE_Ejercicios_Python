#CREAR UN NUEVO ARCHIVO DENOMINADO ejercicio4_ArchivosCSV

#Archivos CSV

#CSV significa Comma-Separated Values (valores separados por comas). Es el formato más común para
# o cualquier editor de texto, y es fácil de leer y escribir desde Python.

# --- Ejercicio 11: Sistema integrador ------------------------
import csv
import os

ARCHIVO_DATOS = "registro_alumnos.csv"
CALIFICACION_MINIMA = 6.0

# --- Funciones de archivo -------------------------------------
def cargar_alumnos():
    """Carga los alumnos desde el CSV. Regresa lista vacía si no existe."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    alumnos = []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                alumnos.append({
                    "nombre": fila["nombre"],
                    "nota":   float(fila["nota"])
                })
    except Exception as e:
        print(f"Error al cargar datos: {e}")
    return alumnos



def guardar_alumnos(alumnos):
    """Guarda la lista de alumnos en el CSV."""
    with open(ARCHIVO_DATOS, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre", "nota"])
        for a in alumnos:
            escritor.writerow([a["nombre"], a["nota"]])

# --- Funciones de operación -----------------------------------
def agregar_alumno(alumnos):
    """Registra un alumno nuevo con validación."""
    nombre = input("Nombre del alumno: ").strip()
    while True:
        try:
            nota = float(input("Calificación (0-10): "))
            if 0 <= nota <= 10:
                break
            print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Ingresa un número válido.")
    alumnos.append({"nombre": nombre, "nota": nota})
    print(f"{nombre} registrado correctamente.")

def buscar_alumno(alumnos, nombre):
    """Busca un alumno por nombre. Regresa el índice o -1."""
    for i, alumno in enumerate(alumnos):
        if alumno["nombre"].lower() == nombre.lower():
            return i
    return -1



def generar_reporte(alumnos):
    """Muestra el reporte completo con estadísticas."""
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    print(f"\n{'Alumno':<15} {'Nota':>6} {'Estado':<12}")
    print("-" * 38)
    total = aprobados = 0
    for a in alumnos:
        estado = "Aprobado" if a["nota"] >= CALIFICACION_MINIMA else "Reprobado"
        print(f"{a['nombre']:<15} {a['nota']:>6.1f} {estado:<12}")
        total += a["nota"]
        aprobados += 1 if a["nota"] >= CALIFICACION_MINIMA else 0
    print("-" * 38)
    print(f"Promedio:   {total/len(alumnos):.2f}")
    print(f"Aprobados:  {aprobados} de {len(alumnos)}")

# --- Menú principal -------------------------------------------
def mostrar_menu():
    print("\n=== Sistema de Calificaciones ===")
    print("1. Registrar alumno")
    print("2. Buscar alumno")
    print("3. Ver reporte")
    print("4. Salir")





def main():
    alumnos = cargar_alumnos()
    print(f"Sistema iniciado. {len(alumnos)} alumnos cargados.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_alumno(alumnos)
            guardar_alumnos(alumnos)
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            idx = buscar_alumno(alumnos, nombre)
            if idx != -1:
                a = alumnos[idx]
                estado = "Aprobado" if a["nota"] >= CALIFICACION_MINIMA else "Reprobado"
                print(f"{a['nombre']}: {a['nota']:.1f} - {estado}")
            else:
                print("Alumno no encontrado.")
        elif opcion == "3":
            generar_reporte(alumnos)
        elif opcion == "4":
            guardar_alumnos(alumnos)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Elige entre 1 y 4.")

main()
