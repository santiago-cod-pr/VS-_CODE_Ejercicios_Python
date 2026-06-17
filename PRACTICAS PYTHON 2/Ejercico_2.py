# Condicional multiple y anidada

# elif (else if) - Agrega ramas intermedias

#Clasificador de calificaciones

nota = float(input("Calificaion (0-10): "))

if nota < 0 or nota >10:
    print("Calificacion invalida")

elif nota >= 9.0:
    letra = "A - Excelente"
    resta = 0
    letra_sig = None

elif nota >= 8.0:
    letra = "B - Bien"
    resta = 9 - nota
    letra_sig = "A"

    
elif nota >= 7.0:
    letra = "C - Suficiente"
    resta = 8 - nota
    letra_sig = "B"


elif nota >= 6.0:
    letra = "D - Aprobado Minimo"
    resta = 7 - nota
    letra_sig = "C"
    

else:
    letra = "F - Reprobado"
    resta = 6 - nota
    letra_sig = "D"

if 0 <= nota <=10:
    print(f"Nota: {nota:.1f} -> {letra}")

    if letra_sig:
        print(f"Faltan {resta:.1f} puntos para llegar a la letra {letra_sig}")
    else:
        print("FELICIDADES, TIENE EL PUNTAJE MAS ALTO!!!")

# Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra. Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.