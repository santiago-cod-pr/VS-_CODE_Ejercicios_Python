# CICLOS ANIDADOS + BREAK Y CONTINUE
#CICLOS ANIDADOS - UN CICLO DENTRO DE OTRO

#Un CICLO ANIDADO es un ciclo dentro del bloque de otro ciclo. Por cada iteracion del ciclo externo, el ciclo interno
#se ejecuta completamente. Total de ejecuciones = iteraciones_externo x iteraciones_interno.

# CUANDO USARLOS: tablas, matrices, patrones, comparacion de dos listas. Si necesitas mas de 2 niveles de anidacion,
#busca antes una solucion mas simple.


#Ejercicio ---- Ciclos anidados: Tabla de multiplicar

#El ciclo externo es la tabla y el interno son las multiplicadores del 1 al 10.

#------- Ejercicio: Tabla de Multiplicar ----------

N = int(input("¿Hasta qué tabla quieres? "))

for tabla in range(1, N + 1):
    print(f"--- Tabla del {tabla} ---")
    for mult in range(1, 11):
        resultado = tabla * mult
        print(f"  {tabla} x {mult:2} = {resultado:3}")
    print()    # línea en blanco entre tablas


#Tu turno: Modifica el Ejercicio para imprimir solo los resultados impares de cada tabla. 
# Necesitarás un if dentro del for interno que verifique si el resultado es impar usando el operador %.

N = int(input("Hasta que tabla quieres (RESULTADOS IMPARES)?: "))

for tabla in range(1, N+1):
    print(f"---- tabla del {tabla} ----")

    for mult in range(1,11):
        resultado = tabla * mult
        if resultado %2 !=0:                                 # <----Tu turno: Modifica el Ejercicio para imprimir solo los resultados impares de cada tabla.
            print(f" {tabla} x {mult:2} = {resultado:3}")
    print("") #linea en blanco entre tablas



#____________________________________________________________________________________________________________________

# break y continue — control del flujo del ciclo

# Estas dos palabras reservadas modifican el comportamiento normal de un ciclo:

#break: termina el ciclo inmediatamente, aunque la condición todavía sea True. El programa continúa después del ciclo.
#continue: salta el resto del bloque actual y pasa a la siguiente iteración. El ciclo NO termina.
#Úsalos con criterio. Abusar de ellos hace el código difícil de seguir. Son válidos cuando simplifican la lógica, no cuando la complican.

# Ejercicio:  break y continue: diferencia en acción
# Observa cómo cada uno altera el flujo del ciclo de forma completamente diferente.

# ── Ejercicio: break y continue ───────────────────────────
    
notas = [9.0, 8.5, 7.0, 4.5, 9.5, 6.0]

# break — sale del ciclo al encontrar el primer reprobado
print("Buscando primer reprobado...")
for i, nota in enumerate(notas):
    if nota < 6.0:
        print(f"  Primer reprobado en posición {i}: {nota}")
        break    # ya encontramos lo que buscábamos
print()

# continue — salta los reprobados, solo procesa aprobados
print("Solo aprobados:")
for nota in notas:
    if nota < 6.0:
        continue    # salta esta iteración, el ciclo continúa
    print(f"  Aprobado: {nota:.1f}")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Tu turno: Reescribe el bloque de "Solo aprobados" del Ejercicio sin usar continue, usando un if normal. 
# ¿El resultado es el mismo? ¿Cuál versión es más fácil de leer?


# Sin continue
print("---------------------------")
print("Solo aprobados:")
for nota in notas:
    if nota >= 6.0:
        print(f"  Aprobado: {nota:.1f}")

# ¿El resultado es el mismo? ¿Cuál versión es más fácil de leer?
#/ RESPUESTA: Es el mismo resultado, la version con el if es mas facil de entender, porque es directa para nuestra logica /