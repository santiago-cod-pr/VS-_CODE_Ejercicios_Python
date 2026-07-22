# Los indices empiezan en 0, no en 1. El primer elemento es lista [0],
# el segundo elemento es lista[1], y el ultimo es lista[len(lista) -1] o lista[-1]

frutas = ["manazana", "fresa", "mango", "pera", "uva"]

#Acceso por indice positivo y negativo
print(frutas[0]) # <--- manzana - Primer elemento
print(frutas[-1])# <--- uva - Ultimo elemento
print(frutas[-2])# <---- pera - penultimo elemento

#Longitud
print(len(frutas)) # 5

#Agregar al final - sandia  (.append) ---> agrega elemento al final del la lista
frutas.append("sandia")
print(frutas)


#Insertar elemento en una posicion especifica - posicion 3  (.insert) ---> agrega elemento en una posicion especififca
frutas.insert(2, "melon")   # declaracion (posicion. valor a agregar)
print(frutas)


#Elimiar por valor - uva  ---> (.remove)
frutas.remove("uva")
print(frutas)

#Elimiacion por indice ---> (del)
del frutas[1]
print (frutas)

# Ordenar  A - Z con (.sort)
frutas.sort()
print(frutas)

# Ordenar  Z - A con (.sort)
frutas.sort(reverse = True)
print(frutas)


#Ejercicio2 - Slicing y recorrida con for
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numeros[2:5]) #Muetsra elementos en ese rango e imprime hasta uno antes del limite
print(numeros[:4]) # Como no hay un inicio definido agarra a partir del primer elemento e imprime hasta uno antes del limite
print(numeros[7:]) # Como no hay un final definido agarra a partir de ese elemento en adelante
print(numeros[::2]) #Imprime cada 2 elementos
print(numeros[::-1]) # Lista invertida

# Recorrido con for
print("\n Recorrido de la llista")
for numero in numeros:
    print(numero, end=" ")
print()

#Recorrido con indice usando enumerate
print("\nCon indice: ")
for i, numero in enumerate(numeros):
    print(f"Posicion {i}: {numero}")