#Cuando ejcutamos el programa sin "Archivos" se carga en la RAM, y se elimina al cerrarlo.

#La forma recomendada de trabajar con archivos em python es usando el bloque with.
#Su ventaja principal es que cierra el archivo automaticamente al salir del bloque, incluso si
#ocurre un error. No hay que llamar al archivo.close() manualmente.

#Escribir y leer archivo de texto
with open("notas.txt", "w", encoding= "utf-8") as archivo:
    archivo.write("Povedano: 9.5\n")
    archivo.write("Santiago: 8.9\n")
    archivo.write("Gissel: 8.4\n")
    archivo.write("Alexandro: 7.3\n")
    archivo.write("Sulub: 6.9")
    
print("Archivo Creado Correctamente")

# LEER - READ() lee todo el contenido de una vez
print("\n----- Contenido con read() -----")
with open("notas.txt", "r", encoding= "utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)