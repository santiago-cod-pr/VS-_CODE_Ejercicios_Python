#SANTIAGO MARTINEZ CAAMAL | TI21
#Condicional anidada: Sistema de acceso
#Usuario y contrasena correcta. Si el Usuario falla, ni siquiera revisa la contrasena

USUARIO_CORRECTO = "santiago"
CONTRASENA_CORRECTA = "2007"

print("=========      LOGIN     ===========")
print("====================================")

print("=== INGRESE USURIO Y CONTRASENA ===")
print("====================================")
print("")
usuario = input( "INGRESE SU USUARIO: ")
contrasena = input("INGRESE SU CONTRASENA: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("ACCESO CONCEDIDO. BIENVENIDO")
else:
    print("USUARIO O CONTRASENA INCORRECTOS.")
