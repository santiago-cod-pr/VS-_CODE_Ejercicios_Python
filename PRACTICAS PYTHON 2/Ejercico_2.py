# Condicional multiple y anidada

# elif (else if) - Agrega ramas intermedias

#Clasificador de calificaciones

nota = float(input("Calificaion (0-10): "))

if nota < 0 or nota >10:
    print("Calificacion invalida")
elif nota >= 9.0:
    letra = "A - Excelente"
elif nota >= 8.0:
    letra = "B - Bien"
elif nota >= 7.0:
    letra = "C - Suficiente"
elif nota >= 6.0:
    letra = "D - Aprobado Minimo"

else:
    letra = "F - Reprobado"

if 0 <= nota <=10:
    print(f"Nota: {nota:.1f} -> {letra}")


# Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra. Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.