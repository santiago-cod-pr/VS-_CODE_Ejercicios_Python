# Elaborado por Santiago Martinez Caamal TI21
# 15 de Julio de 2026


# Constantes para el Menu
OPC_REGISTRAR_USUARIO = "1"
OPC_HISTORIAL = "2"
OPC_SALIR = "3"
# Constantes para Precios:
COSTO_DIA = 50
CARGO = 2


#=====================================================================
# Funciones Recursivas:
#=====================================================================

# Funcion para los dias del prestamo
def dias(dias_de_prestamo):
    #caso base
    if dias_de_prestamo == 1:
        return 1
#caso recursivo:
    return dias(dias_de_prestamo - 1)


#Funcion para el costo por dias:
def costo_por_dias(dias_de_prestamo, COSTO_DIA):
    if dias_de_prestamo == 1:
        return COSTO_DIA
    else:
        total_a_pagar = COSTO_DIA + costo_por_dias(dias_de_prestamo - 1, COSTO_DIA)
        return total_a_pagar

# Funcion para calcular el total a pagar
def calcular_total_a_pagar(dias_de_prestamo):
    costo_dias = costo_por_dias(dias_de_prestamo, COSTO_DIA)
    total = costo_dias + CARGO
    return total

#=====================================================================
# Procedimientos:
#=====================================================================


def Mostrar_menu():
 print("---------------------------------------------------")
 print("\n === FERRETERIA SISTEMA DE VENTAS Y PRESTAMOS ===")
 print("---------------------------------------------------")
 print("----------- // Elija una opcion // ----------------")
 print("---------------------------------------------------")
 print(f"\n{OPC_REGISTRAR_USUARIO}. Registrar nuevo cliente")
 print(f"{OPC_HISTORIAL}. Consultar Historial")
 print(f"{OPC_SALIR}. Salir de Programa")



def historial(nombre_cliente, nombre_herramienta, dias_de_prestamo, Total_a_pagar):
    print("\n=================================================")
    print("=========== REPORTE DE LA SESION ================")
    print("=================================================")
    if not historial:
        print(" !! NO HAY OPERACIONES REGISTRADAS AUN !!")
        return
    
    print("Nombre del cliente: ", nombre_cliente)
    print("Nombre de la herramienta: ", nombre_herramienta)
    print("Dias de prestamo: ", dias_de_prestamo)
    print("Total a pagar: ", Total_a_pagar)





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
    
    print("Nombre del cliente: ", nombre_cliente)
    print("Nombre de la herramienta: ", nombre_herramienta)
    print("Dias de prestamo: ", dias_de_prestamo)
    print("Total a pagar: ", Total_a_pagar)
    
    # Encabezados de la tabla
    print(f"{'No.':<5} {'Operacion':<20} {'Datos':<25} {'Resultado':<15}")
    print("-" * 70)

    # Variables contadores
    prestamos_cobrados_dia = 0
    nombre_cliente = []
    nombre_herramienta = 0
    dias_de_prestamo = 0
    Total_a_pagar = 0

    for op in historial:
        print(f"{op['no']:<5} {op['tipo']:<20} {op['datos']:<25} {op['nombre_d_herramienta']:<15}")

    # Conteo por el tipo de operacion
        if op['tipo'] == "Prestamo":
            c_potencia += 1
        

    print ("-" * 70)
    print(f"Prestamos registrados:       {prestamos_cobrados_dia}")





def mostrar_reporte(nombre_cliente, nombre_herramienta, dias_de_prestamo, Total_a_pagar):
    print("---------------------------------------------------")
    print("\n === FERRETERIA SISTEMA DE VENTAS Y PRESTAMOS ===")
    print("----------- // REPORTE DE PRESTAMO // -------------")
    print("Nombre del cliente: ", nombre_cliente)
    print("Nombre de la herramienta: ", nombre_herramienta)
    print("Dias de prestamo: ", dias_de_prestamo)
    print("Total a pagar: ", Total_a_pagar)





# ============================================================
#   FLUJO DEL PROGRAMA:
# ============================================================

def main():
    historial = []
    numero_operacion = 1

    while True:
        Mostrar_menu()
        opcion = input("\nElija la operacion que desea Realizar:").strip()


        if opcion == OPC_REGISTRAR_USUARIO:
            print("\n === REGISTRO DE NUEVO CLIENTE ===")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            nombre_herramienta = input("Ingrese el nombre de la herramienta: ")
            dias_de_prestamo = int(input("Ingrese los dias de prestamo: "))
            Total_a_pagar = calcular_total_a_pagar(dias_de_prestamo)
            print(f"Total a pagar sera: ${Total_a_pagar:.2f} ")

            historial.append({
                "no": numero_operacion,
                "tipo": "Prestamo",
                "datos": f"Cliente: {nombre_cliente}, Herramienta: {nombre_herramienta}",
                "resultado": f"Dias: {dias_de_prestamo}, Total: ${Total_a_pagar:.2f}"
            })
            numero_operacion += 1


        elif opcion == OPC_HISTORIAL:
             mostrar_reporte(historial)


if __name__ == "__main__":
    main() 