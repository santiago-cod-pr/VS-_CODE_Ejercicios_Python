#SANTIAGO MARTINEZ CAAMAL | TI21


#Ejercicio
#Condicional anidada: Sistema de acceso
#Usuario correcto Y contraseña correcta. Si el usuario falla, ni siquiera revisa #la contraseña.

# ── Ejercicio 5: if anidado — sistema de acceso ───────────────
USUARIO_CORRECTO    = "admin"
CONTRASENA_CORRECTA = "1234"

usuario    = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == USUARIO_CORRECTO:
    # Solo llegamos aquí si el usuario es correcto
    if contrasena == CONTRASENA_CORRECTA:
        print("Acceso concedido. Bienvenido.")
    else:
        print("Usuario correcto pero contraseña incorrecta.")
else:
    print("Usuario no reconocido.")

#_______________________________________________________________________________________________________________________________________________

#Tu turno: Reescribe el Ejercicio  usando una sola condición con and en lugar del if anidado.
# Luego compara las dos versiones: ¿cuál da mensajes de error más específicos y por qué?

#RESPUESTA: El primer ejercicio de if anidado da el mensaje mas especifico, ya que da a conocer al usuario donde tuvo el error,
#indica si fue el usuario o la contrasena donde esta el detalle, en cambio la condicion "and", no nos da donde se podria encontar el error.

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
