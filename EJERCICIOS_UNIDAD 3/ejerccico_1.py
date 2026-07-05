# Que es un subprograma?
#Un subprograma es un bloque de codigo independiente,
#con su propio nombre, que realiza una tarea especifica y puede ser invocado (llamado)
#desde cualquier parte del programa principal, las veces que necesite.

#-------------------------------------------------------------------------------------------------------------------
#FUNCIONES Y PROCEDIMIENTOS:

#FUNCION: es el subprograma que SIEMPRE regresa un valor al punto donde fue llamado, usando la sentencia return.
#Se usa cuando necesitas un resultado para seguir trabajando con el.

#PROCEDIMIENTO: Subprograma que realiza una accion (mostrar algo, modificar datos, guardar informacion),
#pero no necesariamente regresa un valor utilizable, se usa cuando el objetivo es ejecutar una tarea,
#  no obtener un dato de vuelta. NO USA EL return AL FINAL
#se hace colocando: def
#public static int sumar(int a, int b){ return a + b}  ----> en JAVA
#-------------------------------------------------------------------------------------------------------------------

#EJERCICIO 1: funcion vs Procedimiento:
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area # <-- regresa un valor: es FUNCION

def mostrar_resultado(nombre, area):
    print(f"El area de {nombre} es {area} M2") # <-- No regresa nada es PROCEDIMIENTO


#Uso de ambos subprogramas:
resultado = calcular_area_rectangulo(5,5)
mostrar_resultado("el terreno", resultado )

#-------------------------------------------------------------------------------------------------------------------

# Tu turno: Escribe un procedimiento llamado saludar (nombre) que imprima un saludo personalizado, y una
#funcion llamada es_mayor_de_edad(edad) que regrese True o False. Usa ambos en un mini programa.

nombre2 = input("Ingrese su Nombre: ")
edad = int(input("Ingrese su edad para saber si es MAYOR o MENOR de edad: "))

def saludar (nombre2):
    print(f"\nHola {nombre2} How are you tuday :)?")
    

def es_mayor_de_edad (edad):
    return edad >= 18


#Uso de ambos subprogramas:
saludar(nombre2)
if es_mayor_de_edad (edad):
    print("es Mayor de edad :)")
else:
    print ("NO es mayor de edad :(")


#-------------------------------------------------------------------------------------------------------------------

def calcular_doble(numero):
    doble = numero * 2
    print (doble)

resultado = calcular_doble(10)
print (resultado)
    
#Tu turno: Corrige el Ejercicio 2 para que calcular_doble regrese el valor correctamente
# con return, y que sea el print(resultado) el que se encargue de mostrarlo.

def calcular_doble(numero):
    doble = numero * 2
    return doble

resultado = calcular_doble(10)
print (resultado)