#SANTIAGO MARTINEZ CAAMAL | TI21
#Condicional anidada: Sistema de acceso
#Usuario y contrasena correcta. Si el Usuario falla, ni siquiera revisa la contrasena


#Tu turno: Reescribe el Ejercicio  usando una sola condición con and en lugar del if anidado. Luego compara las dos versiones: ¿cuál da mensajes de error más específicos y por qué?

USUARIO_CORRECTO = "santiago"
CONTRASEÑA_CORRECTA = "2007"

print("=========      LOGIN     ===========")
print("====================================")
print("=== INGRESE USUARIO Y CONTRASEÑA ===")
print("====================================")
print("")
usuario = input( "INGRESE SU USUARIO: ")
contrasena = input("INGRESE SU CONTRASEÑA: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASEÑA_CORRECTA:
    print("ACCESO CONCEDIDO. BIENVENIDO")
else:
    print("USUARIO O CONTRASEÑA INCORRECTOS.")
