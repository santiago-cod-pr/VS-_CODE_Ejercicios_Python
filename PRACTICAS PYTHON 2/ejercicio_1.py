# Python usa la sangria (espacios al inicio de la linea) para delimitar bloques de codigo {}, python usa 4 espacios por nivel con TAB (USA SANGRIAS para la IDENTACION), Esta es la diferencia visual mas importante entre python y otros lenguajes.

#if condicion:
#    instruccion1
#else:
#    instruccion2

#Toda estructura de control termina su primera linea con dos puntos ":". Los dis puntos le dicen a Python: el bloque de esta estructura cominenza en la siguiente linea. SI se omiten, Python genera SyntaxError: expexted ":"

# = asignar un valor
# == comparar dos valores igual que
# ===
# != Diferente de
# > mayor que / >= mayor o igual
# < menor que / <= menor o igual
# AND Ambas condiciones True / OR Al menos una es True / NOT Negacion logica


# IF ejecuta un bloque unicamente si la condicion es True. Si la condicion es False, el bloque se salta por completo y el programa continua. Solo tiene una rama posible

# CONDICION SIMPLE
nota = 8.5

if nota >= 6.0:
    print("El alumno Aprobo")

print("Fin del programa")

#CONDICION DOBLE - IF/ELSE
#El else granatiza que SIEMPRE se ejecita algo. Sin importar si la condicion es TRUE o FALSE, el programa toma uno de los dos caminos. Nunca quedan casos sin respuesta.

# Ejercicio 2
CALIFICACION_MINIMA = 7.0
nota = float(input("Ingresa tu calificacion: "))

if nota >= CALIFICACION_MINIMA:
    print(f"Aprobado con {nota:.1f}")
else:
    print(f"Reprobado con {nota:.1f}")
    faltaron = CALIFICACION_MINIMA - nota
    print(f"Te faltaron {faltaron:.1f} puntos para aprobar")


    # Condiciones compuestas: AND / OR en accion

    edad = int(input("Tu edad: "))
    tiene_INE = input("Tiene INE (Si / NO): ")

    if edad >= 18 and tiene_INE == "si":
        print("Puedes Votar")
    else:
        print("No puedes votar aun")

        # Validacion de rango con "AND" y "OR"
    calificacion = float(input("Calificaion (0-10): "))

    if calificacion <0 or calificacion > 10:
        print("Calificacion fuera de rango")
    else:
        print(f"Calificacion registrada: {calificacion:.1f}")
        

# Tu turno: Crea una condición que verifique si un año es bisiesto. Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100, también debe ser divisible entre 400. Pista: usa el operador % (módulo).


año = int(input("INTRODUZCA EL AÑO PARA SABER SI ES BISIESTO: "))
           
if año % 4 == 0:
     if año % 100 == 0:
          if año % 400 == 0:
              
              print(f"El año: {año} ES BISIESTO !!!!")
          else:
              print(f"El año: {año} NO ES BISISESTO ****")

     else:
    #Si es divisble entre 4 pero NO entre 100
            print(f"El año: {año} es bisiesto")

# Si el año NO es divisble entre 4 se DESCARTA aqui:
else:
    print(f"El año: {año} NO ES BISIESTO. ***")





#Opcion con elif:


año = int(input("Introduce un año: "))

# 1. El filtro más pesado: si es de cambio de siglo, revisamos el 400 de una vez
if año % 400 == 0:
    print(f"El año {año} es bisiesto.")

# 2. Si no fue el anterior, pero es divisible entre 100, se descarta (no es bisiesto)
elif año % 100 == 0:
    print(f"El año {año} NO es bisiesto.")

# 3. Si no cumplió las anteriores, pero sí es divisible entre 4, sí es bisiesto
elif año % 4 == 0:
    print(f"El año {año} es bisiesto.")

# 4. Cualquier otra cosa (como un número impar) no es bisiesto
else:
    print(f"El año {año} NO es bisiesto.")

