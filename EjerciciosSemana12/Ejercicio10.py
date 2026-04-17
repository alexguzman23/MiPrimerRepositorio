# Ejercicio 10: Pide usuario y contraseña.
# Si ambos coinciden con valores predefinidos,
# muestra "Acceso permitido", de lo contrario "Acceso denegado".

usuario_correcto = "pezahogado"
password_correcto = "2023"


intentos_usuario = input("Usuario: ")
intentos_password = input("Contraseña: ")


if intentos_usuario == usuario_correcto and intentos_password == password_correcto:
    print("Acceso permitido")
else:
    print("Acceso denegado")
