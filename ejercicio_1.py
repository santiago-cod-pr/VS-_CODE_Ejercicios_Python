
#REALIZADO POR: SANTIAGO_MARTINEZ_PDC
# Este es un comentario de una linea
#Que ocua varias lineas
#(EJEMPLO DE COMENTARIOS)

"""
esta es una prueba
de lineas

(EJEMPLO DE COMENTARIOS)

"""

entero = 42 #Numeros enteros
decimal = 3.1416 #Numeros Decimlaes (Float)
logico = True #Boolean
nombre = "juan" #String

#DECLARA VARIABLES QUE ALMACENEN TU NOMBRE, APELLIDO: PATERNO Y MATERNO Y EDAD.

nombre = "Santiago"
apellido_paterno = "Martinez"
apellido_materno = "Caamal"
Edad = "18 años"
Estatura = 1.70

print(" ")
print (nombre)
print (apellido_paterno)
print (apellido_materno)
print (Edad)
print (Estatura)

print (entero);
print (decimal);
print (logico);
print (nombre);
print("")


# TIPOS DE DATOS PRIMITIVOS: list, tuple, set, dict, arrays, range, frozenset, nontype, complex

#Str - inmutable
nombreMateria = "Programacion"
print (nombreMateria[0])
print (nombreMateria[-1])
print (nombreMateria[0:6])
print("")

#List - mutable (USO DE CORCHETES)
calificaciones = [8.5, 9.0, 7.5, 10.0]
calificaciones.append(9.5)
calificaciones[0] = 8.0
print(calificaciones)
print("")

#TUPLE - INMUTABLE: (ordenado pero no se puede modificar) (USO DE PARENTESIS)
coordenadas = (19.4326, -99.1332) 
print(coordenadas[0])
print("")

# DICT - Clave:Valor  (USO DE LLAVES)
alumno = {"nombre": "Santiago", "edad": 28, "promedio": 9.4}
print(alumno["nombre"])
alumno ["promedio"] = 9.6  #para modificar calificaion.
print (alumno)
print("")




# CREA UN DICCIONARIO CON TUS DATOS: NOMBRE, EDAD Y MATERIA FAVORITA. IMPRIME SOLO TU NOMBRE ACCEDIENDO A LA CLAVE CORRECTA:

infor = {"nombre1": "Santiago", "edad": 18, "Materia Favorita": "Conmutacion y Enrutamiento de Redes"}
print (infor["nombre1"])
