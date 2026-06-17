# CICLO WHILE - Repite un vloque    MIENTRAS una condicion sea true. Se usa cuando NO sabes de antemano cuantas veces necesitas repetir - el numero de repeticiones depende de lo que ocurra durante la ejecucion.

#regla critica: algo dentro de del while DEBE ambiar en cada iteracion para que la condicion eventualmente sea false. Sin esto, el ciclo nunca termina.

#Ejercicio - While basico: contador y acumulador
N = int(input("suma del 1 hasta: "))
i = 1 # contador - empieza en 1
suma = 0 #Acumulador - empieza en 0

while i <= N:
    suma = suma + i
    i = i + 1
print(f"suma de 1 a {N}: {suma}")

# VERIFICAION MATEMATICA: N * (N + 1)/2
formula =  N * (N + 1)//2
print(f"Verificacion con formula: {formula}")

#Tu turno: Reescribe el ejercicio usando for en lugar de while. ¿Cuál versión es más natural para este problema? Explica por qué con tus palabras.



# Ejercicio - While para validar entrada: el patron de reinicio

nota = float(input("Calificacion (0 - 10): "))
             
while nota <0 or nota > 10:
    print("Calificacion invalida. Debe ser entre 0 y 10.")
    nota = float(input("Calificacion (0-10)"))

print(f"Calificacion Registrada: {nota:.1f}")
print("")


# While True + break
while True:
    edad = int(input("Tu edad(1-80)"))
    if 1 <= edad <= 80:
        break
    print("Edad invalida, Intenta de nuevo.")

print(f"Edad Registrada: {edad}")

#Tu turno: Crea un programa que pida al usuario adivinar un número secreto (define tú el número con una constante). Con while, sigue pidiendo hasta que lo adivine e imprime cuántos intentos necesitó.
