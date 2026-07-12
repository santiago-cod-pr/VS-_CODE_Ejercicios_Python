# ELABORADO POR SANTIAGO MARTINEZ CAAMAL TI21
# 12 DE JULIO DE 2026.

# Constantes para el Menu
OPC_POTENCIA = "1"
OPC_SUMA_ACUM = "2"
OPC_FACTORIAL = "3"
OPC_SUMA_DIGITOS = "4"
OPC_REPORTE = "5"
OPC_SALIR = "6"

#=====================================================================
# Funciones Recursivas:
#=====================================================================


# /// FUNCION PARA CALCULAR PORTENCIAS ///
def calcular_potencia(base, exponente):
    """
    Calcula de manera recursiva la potencia de un numero
    RECIBE: base (int / float), exponente (int >= 0)
    REGRESA: resultado del exponente (int / float)
    """
#Caso base: numero elevado a 0 = 1
    if exponente == 0:
        return 1
#Caso Recursivo
    return base * calcular_potencia(base, exponente - 1)


# /// FUNCION PARA CALCULAR SUMA ACUMULADA ///
def calcular_suma_acumulada(n):
    """
    Calcula la suma de 1 hasta n de manera recursiva
    RECIBE: n (int > 0)
    REGRESA: int (suma acumulada)
    """
#Caso base: la suma hasta 1 es 1
    if n == 1:
        return 1
#Caso recursivo
    return n + calcular_suma_acumulada(n-1)


# /// FUNCION PARA CALCULAR FACTORIAL ///
def calcular_factorial(n):
    """
    Calcula de manera recursiva el factorial de un numero n
    RECIBE: int (n >= 0)
    REGRESA: int (Factorial de n)
    """
#Caso base: el factorial de 0 o 1 = 1
    if n == 0 or n == 1:
        return 1
#Caso recursivo
    return n * calcular_factorial(n-1)


# /// FUNCION PARA SUMAR DIGITOS ///
def calcular_suma_digitos(n):
    """
Calcula de forma recursiva la suma de los digitos de un numero
RECIBE: n (int positivo)
REGRESA: int (suma de los digitos de ese numero)
"""
#Caso base: si le numero tiene un solo digito
    if n < 10:
     return n
#Caso recursivo: ultimo digito + suma del resto del numero
    return (n % 10) + calcular_suma_digitos(n // 10)



#=====================================================================
# Procedimientos:
#=====================================================================


def mostrar_menu():
    "Muestra las opciones del menu en pantalla:"
    print("---------------------------------------------------")
    print("\n === Practica de Operaciones Matematicas UTRM ===")
    print("---------------- Elija una opcion -----------------")
    print(f"{OPC_POTENCIA}. Calcular una Potencia.")
    print(f"{OPC_SUMA_ACUM}. Calcular suma acumulada.")
    print(f"{OPC_FACTORIAL}. Calcular Factorial.")
    print(f"{OPC_SUMA_DIGITOS}. Calcular la suma de digitos de un numero.")
    print(f"{OPC_REPORTE}. Consulte reporte de la Sesion.")
    print(f"{OPC_SALIR}. Salir de este programa.")


def mostrar_reporte(historial):
    """
    Muestra una tabla ordenada del historial de operaciones y al final anade el conteo estadistico por tipo
    RECIBE: El historial (list de dicts)
    """
    print("\n=================================================")
    print("=========== REPORTE DE LA SESION ================")
    print("=================================================")

    if not historial:
        print(" !! NO HAY OPERACIONES REGISTRADAS AUN !!")
        return
    
    # Encabezados de la tabla
    print(f"{'No.':<5} {'Operacion':<20} {'Datos':<25} {'Resultado':<15}")
    print("-" * 70)

    # Variables contadores para Extension 2
    c_potencia = 0
    c_suma_acumulada = 0
    c_factorial = 0
    c_suma_digitos = 0

    for op in historial:
        print(f"{op['no']:<5} {op['tipo']:<20} {op['datos']:<25} {op['resultado']:<15}")

    # Conteo por el tipo de operacion
        if op['tipo'] == "Potencia":
            c_potencia += 1
        elif op['tipo'] == "Suma Acumulada":
            c_suma_acumulada += 1
        elif op['tipo'] == "Factorial":
            c_factorial += 1
        elif op['tipo'] == "Suma de Digitos":
            c_suma_digitos += 1

    print ("-" * 70)

# Impresión de estadisticas solicitadas en la Extensión 2
    print(f"Potencias calculadas:        {c_potencia}")
    print(f"Sumas acumuladas calculadas: {c_suma_acumulada}")
    print(f"Factoriales calculados:      {c_factorial}")
    print(f"Sumas de digitos calculadas: {c_suma_digitos}")
    print(f"Total de operaciones:        {len(historial)}")



# ============================================================
#   FLUJO DEL PROGRAMA:
# ============================================================

def main():
    historial = []
    numero_operacion = 1

    while True:
        mostrar_menu()
        opcion = input("\nElija la operacion que desea Realizar:").strip()

         #Bloque para la opcion de Potencia:

        if opcion == OPC_POTENCIA:
         #Validacion de la base:
            while True:
                try:
                    base = int(input("POTENCIA -Ingrese la Base: "))
                    break
                except ValueError:
                   print("!! ERROR: Ingrese un Numero Valido !!")

            #Validacion del exponente (No puede ser negativo):
            while True:
                try:
                    exponente = int(input("POTENCIA - Ingrese el Exponente: "))
                    if exponente >= 0:
                        break
                    print("!! ERROR: El exponente NO PUEDE ser NEGATIVO !!")
                except ValueError:
                    print("!! ERROR: Ingrese un Numero Entero Valido !!")    

            resultado = calcular_potencia(base, exponente)
            print(f"Resultado: {base} ^ {exponente} = {resultado}")

            historial.append({
                'no': numero_operacion,
                'tipo': "Potencia",
                'datos': f"Base = {base}, exp = {exponente}",
                "resultado": resultado
            })
            numero_operacion +=1


            #Bloque para la opcion de Suma Acumulada:

        elif opcion == OPC_SUMA_ACUM:
            # Validacion: Debe ser positivo mayor a cero
            while True:
                try:
                    n = int(input("SUMA ACUMULADA - Ingrese Un Numero (debe ser mayor a cero): "))
                    if n > 0:
                        break
                    print("Error: El número debe ser mayor a cero.")
                except ValueError:
                    print("Error: Por favor, introduce un número entero válido.")

            resultado = calcular_suma_acumulada(n)
            print(f"RESULTADO DE SUMA ACUMULADA DE 1 HASTA {n} = {resultado}")
            historial.append({
                'no': numero_operacion,
                'tipo': "Suma Acumulada",
                'datos': f"n={n}",
                'resultado': resultado
            })
            numero_operacion += 1


            #Bloque para la opcion de Factorial:

        elif opcion == OPC_FACTORIAL:
            # Validación: debe ser entero positivo mayor o igual a cero
            while True:
                try:
                    n = int(input("FACTORIAL - Ingrese Un Numero (debe ser mayor o igual a cero): "))
                    if n >= 0:
                        break
                    print("!!! Error: El número para el factorial debe ser mayor o igual a cero !!!")
                except ValueError:
                    print("Error: Por favor, introduce un número entero válido.")
            
            resultado = calcular_factorial(n)
            print(f"Resultado: {n}! = {resultado}")
            
            historial.append({
                'no': numero_operacion,
                'tipo': "Factorial",
                'datos': f"n={n}",
                'resultado': resultado
            })
            numero_operacion += 1 

        elif opcion == OPC_REPORTE:
            mostrar_reporte(historial)

        elif opcion == OPC_SUMA_DIGITOS:
            # Validación: entero positivo
            while True:
                try:
                    n = int(input("SUMA DE DIGITOS - Número entero positivo: "))
                    if n >= 0:
                        break
                    print("!!! Error: El número debe ser positivo !!!")
                except ValueError:
                    print("!!! Error: Por favor, introduce un número entero válido !!!")
            
            resultado = calcular_suma_digitos(n)
            print(f"Resultado: La suma de los dígitos de {n} es = {resultado}")
            
            historial.append({
                'no': numero_operacion,
                'tipo': "Suma de Digitos",
                'datos': f"n={n}",
                'resultado': resultado
            })
            numero_operacion += 1

        elif opcion == OPC_SALIR:
            print("\n¡Gracias por usar el sistema de la Academia de Matemáticas! Hasta luego.")
            break
        
        else:
            print("\n!!! Error: Opción inválida. Por favor, selecciona una opción del menú !!!")


# Ejecución del programa
if __name__ == "__main__":
    main()    
