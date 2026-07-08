#La recursividad es cuando una función se llama a sí misma para resolver un problema,
#dividiéndolo en una versión más pequeña del mismo problema, hasta llegar a un punto tan simple
#que ya no necesita dividirse más.
"""
def contar_sinlimite(numero):
    print (numero)
    contar_sinlimite(numero +1) # Se llama a si mismo SIEMPRE
    # NO HAY NINGUNA CONDICION QUE DETENGA ESTO

contar_sinlimite(1)
"""
#------ EJERCICIOS FATORIALES ---------------------------------------------------------------------------------

def factiorial_iterativa(n):
    resultado = 1
    for i in range (1, n+1):
        resultado =  resultado * i
    return resultado

print(f"Factorial iterativo de 6: {factiorial_iterativa(6)}")

#           ((((   ITERATIVO = Que se va incrementando   )))))
#Caso base = es la condicion que detiene la recursion. Sin el, la funcion de llamaria infinitamente.
#CASO RECURSIVO = DONDE LA FUNCION SE LLAMA A SI MISMA CON UN PROBLEMA MAS PEQUENO, ACERCANDOSE AL CASO BASE


def factorial_recursivo(n):
    if n == 0 or n == 1: # CASO BASE (EN ESTE CASO NO ES NECESARIO COLOCAR == 0, por si acaso nomas)
        return 1
    else: # CASO RECURSIVO
        return n * factorial_recursivo(n-1)
print(f"Factorial recursivo de 5: {factorial_recursivo(5)}")

#-----------------------------------------------------------------------------------------------------------
#CARACTERISTICAS DE LOS PROCESOS RECURSIVOS:
#La Pila de llamada (Call Stack) ---> almacena hasta llegar al caso base.

def factorial_visual(n, nivel=0):
    sangria = " " * nivel
    print(f"{sangria} --> Entrando con n = {n}")

    if n == 0 or n == 1:
        print(f"{sangria} <-- Caso Base, regresa 1")
        return 1
    else:
        resultado = n * factorial_visual(n - 1, nivel + 1)
        print(f"{sangria} <-- Regresa {resultado} (n = {n})")
        return resultado

factorial_visual(4)

#-----------------------------------------------------------------------------------------------------------

def FIBONACCI(n):
    if n == 0:  # CASO BASE 1
        return 0
    elif n == 1:    # CASO BASE 2
        return 1
    else: # CASO RECURSIVO
        return FIBONACCI(n - 1) + FIBONACCI (n - 2)


for i in range(10):
    print(f"fibonacci ({i}) = {FIBONACCI (i)}")