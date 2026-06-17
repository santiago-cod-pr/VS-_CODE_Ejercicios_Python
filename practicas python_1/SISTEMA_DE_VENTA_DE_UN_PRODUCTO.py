# ELABORADO POR SANTIAGO MARTINEZ CAAMAL TI21
# 09 DE JUNIO DE 2026 | PROGRAMACION ESTRUCTURADA
#---------------------------------------------------------------------------

#Constantes:
IVA = 0.16
DESCUENTO = 0.10

#datos de entrada:
print ("========================================================")
print ("            BIENVENIDO AL SERVICIO DE VENTA             ")
print ("========================================================")

cliente = input("Nombre del cliente: ")
print ("-----------------------------------------------------")
print ("            Que producto desea Comprar?             ")
print ("-----------------------------------------------------")
producto = input("Nombre del producto: ")
Precio_prod = float (input("Precio unitario: "))
Cant_Prod = int(input("Cuantos productos ha elegido: "))

#Calculos:
Subtotal = Precio_prod * Cant_Prod #El subtotal multiplicando el precio unitario por la cantidad de productos
calculo_descuento = Subtotal * DESCUENTO # Cantidad que servira para hacer el descuento
subtotal_con_descuento = Subtotal - calculo_descuento # Subtotal con el descuento aplicado
Precio_con_IVA = subtotal_con_descuento * IVA #Calculo para hallar el IVA
Precio_Final = subtotal_con_descuento + Precio_con_IVA #Precio final con IVA incluido.
print("")
print ("=====================================================")
print ("                TICKET DE COMPRA                     ")
print ("=====================================================")
print ("=  DATOS DEL CLIENTE:                                ")
print ("=", cliente,                                          )
print (type (cliente),                                        )
print ("=====================================================")
print ("=                 DATOS DEL PRODUCTO:                ")
print ("=====================================================")
print ("= PRODUCTO:", producto,                               )
print ("=", type (producto),                                  )
print ("= CANT. DE PROUCTOS:", Cant_Prod,                     )
print ("=", type (Cant_Prod),                                 )
print (f"= PRECIO UNITARIO: $ {Precio_prod:.2f}"              )
print ("=", type (Precio_prod),                               )
print ("=====================================================")
print ("=                 MONTO A PAGAR:                     ")
print ("=====================================================")
print (f"= SUBTOTAL: $ {Subtotal:.2f}",                       )
print (f"= SUBTOTAL CON DESCUENTO DEL 10%: ${subtotal_con_descuento:.2f}" )
print (f"= IVA: $ {Precio_con_IVA:.2f}                 "    )
print (f"TOTAL A PAGAR= ${Precio_Final:.2f}"                 )
print ("====================================================")


