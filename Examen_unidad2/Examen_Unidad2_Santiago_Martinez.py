#Codigo realizado por Santiago Martinez | TI21

print("==================================================================")
print("                         VENTAS DEL DIA")
print("==================================================================")

#variables con listas vacias (Se rellenan con el metodo .append)
ventas_registradas = []
numero_vendedores = []
nombres = []
monto_venta = []


ventas_registradas = int(input("Ingrese el numero de ventas que registrara: "))

for i in range(ventas_registradas):
    print(f"\n --- venta : {i + 1}")
    nombre =input("Ingrese el nombre del vendedor: ")

    while True:
     try:
        monto_de_venta = float(input("Ingrese el monto de la Venta: $"))
        if 0.0 <= monto_de_venta:
            break
        else:
            print(" ** ERROR INGRESE UN NUMERO SUPERIOR A CERO **")
     except:
        print("## Ingrese un numero Valido ##")

    nombres.append(nombre)      #< ---  captura de datos para rellenar "nombres" con el metodo .append
    monto_venta.append(monto_de_venta)      #< ---  captura de datos para rellenar "monto_venta" con el metodo .append

#Encabezados de la tabla del resumen:
print("\n==================================================================")
print("                     REPORTE DE COMISIONES       ")
print("==================================================================")

print(f"{'vendedor' :<20} {'Monto':<20} {'Comision %' :<15} {'Comision %' :<15}")


#Condiciones para asignar porcentaje de comisiones:

for i in range(len(nombres)):
    nombre_actual = nombres[i]
    monto_actual = monto_venta[i]
    if monto_actual < 500:         
        porcentaje = 3
    elif monto_actual <= 1999.99:   
        porcentaje = 5
    elif monto_actual <= 4999.99:   
        porcentaje = 8
    else:
        porcentaje = 12


    comision_pesos = monto_actual * (porcentaje / 100)


    print(f"{nombre_actual:<20} {monto_actual:<20} {porcentaje:<14}% ${comision_pesos:<14.2f}")
print("-" *70)






