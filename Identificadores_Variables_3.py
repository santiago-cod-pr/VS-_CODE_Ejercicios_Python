# IDENTIFIFCADORES Y VARIABLES
# Variables con snake_case

#// Quiero obtener el nombre de un alumno. COMO DEBO DEFINIR MI IDENTIFICADOR?//

nombre_alumno = "Santiago Martinez"
edad_alumno = 18
promedio_final = 9.6

#Constantes con SCREAMING SNAKE CASE  // VARIABLES YA DEINIDAS
TASA_IVA = 0.16
CALIFICACION_MINIMA = 7.0
PESO_PARCIAL = 0.29
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25


#Tipado dinamico - la variable cambia de tipo
dato = 100
print (type(dato))
dato = "cien"
print (type(dato))

#USO DE CONSTANTES EN UN CALCULO
precio_base = 500.0
precio_final = precio_base * (1 + TASA_IVA)   ##// Por regla algebraica, multiplicar cualquier número por 1 da como resultado el mismo número (500 * 1 = 500).
print(f"Precio con IVA:  ${precio_final:.2f}") ## // f = 

print("")


## // DEFINE 3 CONSTANTES: PESO_ PARCIAL = 0.20, PESO_PROYECTO = 0.40 Y CALIFICACION_MINIMA= 6.0. LUEGO CREA 4 VARIABLES CON CALIFICACIONES Y CALCULA EL PROMEDIO USANDO LAS CONSTANTES. IMPRIME SI EL ALUMNO APROBO O REPROBO.
PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICACION_MINIMA = 6.0

parcial_1 = float(input("Ingresa la calificaion parcial 1 : "))
parcial_2 = float(input("Ingresa la calificaion parcial 2 : "))
parcial_3 = float(input("Ingresa la calificaion parcial 3 : "))
parcial_4 = float(input("Ingresa la calificaion parcial 4 : "))

promedio_final1 = (parcial_1 + parcial_2 + parcial_3 + parcial_4) * PESO_PARCIAL
print(promedio_final1)
print("APROBADO" if promedio_final1 >= CALIFICACION_MINIMA else "REPROBADO")