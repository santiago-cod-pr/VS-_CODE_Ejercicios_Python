# - Casting Basico
# Implicita: Int + Float = Float automaticaente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

print("")

#Emplicita: Str a Int
texto_numero = "42"
texto_real = int(texto_numero)
print( texto_real + 8)

print("")

#Explicito> int a Str para concatenar
edad = 28
mensaje = "hola, Soy Juan y mi edad es " + str(edad)
print (mensaje)

print("")

#Float a int
precio = 9.99
print (int(precio))

numero = 7.35
redondeado = round(numero)
print(redondeado)

print("")

#SIMULAREMOS INPUT CON VARIABLES CON VARIABLES FIJAS
dato_usuario = "25"
print(type(dato_usuario))
#print (dato_usuario + 5) # /// error en esta linea, correccion abajo ///
edad_correcta = int (dato_usuario)
print(edad_correcta + 5)


#Patron correcto para entrada de datos ::: //Input = detecta simpre texto//
#edad = int(input("Ingresa tu edad: "))

#// ESCRIBE UN PROGRAMA QUE PIDA AL USUARIO SU NOMRE (STR) Y SU ANO DE NACIMIENTO (INT). CALCULA E IMPRIME SU EDAD APROXIMADA RESTANDO AL ANO ACTUAL (2026).
name = input ("Ingresa tu nombre: ")
date = int(input("Ingresa tu ano de nacimiento: "))
print("Tu nombre es: ", name)
age = 2026 - date
print("tu edad es: ", age)