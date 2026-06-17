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