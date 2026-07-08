#Sintaxis de una funcion

#Encabezado - inicia con la palabra:
#def nombre_funcion(Parametros): --> DEFINE EL NOMBRE Y QUE RECIBE ((Parametros) que datos va a recibe)

#Cuerpo - las lineas de codigo indentadas que ejecutan la logica de la funcion.

#Paramteros - Los datos que la funcion recibe para trabajo (Pueden ser cero, uno o varios).

#Retorno - La sentencia return valor que entrega el resultado de vuelta.

def calcular_promedio(nota1, nota2, nota3): # ----> ENCABEZADO DE MI FUNCION
    suma = nota1 + nota2 + nota3    # <----- CUERPO DE LA FUNCION
    promedio = suma / 3
    return promedio     # <---- RETORNO

resultado = calcular_promedio(8.0, 9.0, 7.0)
print(f"Promedio: {resultado:.2f}")

# ==Tu turno: Modifica la función para que reciba 4 calificaciones
#en lugar de 3, y ajusta el cálculo del promedio correctamente.

def calcular_promedio2(notas1, notas2, notas3, notas4):
    suma2 = notas1 + notas2 + notas3 + notas4
    promedio2 = suma2 / 4
    return promedio2
resultado2 = calcular_promedio2(7.8, 8.9, 9.0, 10)
print(f"Promedio2:{resultado2:.2f}")

#---------------------------------------------------------------------------------------------

def mostrar_bienvenida():                  # -----> PROCEDIMIENTO
    print("=== Sistema de calificaciones ===") #Sin parametros

def calcular_iva(precio, tasa = 0.16): # -->Parametro con valor por defecto
    return precio * (1 + tasa)

#LLAMADA DE FUNCIONES:
mostrar_bienvenida()            # -----> LLAMADA DEL PROCEDIMIENTO

total = calcular_iva(100) # -----> LLAMADA DE LA FUNCION / 100 del precio, la tasa ya esta definida
print(f"Total con IVA por defecto: ${total:.2f}")

total2 = calcular_iva(100, 0.08) #Especificandouna tasa diferente
print(f"Total con IVA especial: ${total2:.2f}")

#---------------------------------------------------------------------------------------------
#Tu turno: Escribe una función calcular_descuento(precio, porcentaje=10) que calcule el precio final con descuento. 
#Pruébala una vez sin especificar el porcentaje y otra vez con un porcentaje distinto.

def calcular_descuento(precio3, porcentaje = 0.10):
    precio_prod = precio3 * (1 - porcentaje)
    precio_final = precio3 - precio_prod
    return precio_final

mostrar = calcular_descuento(100)
print(f"El precio del producto: con descuemto queda:{mostrar:.2f}")