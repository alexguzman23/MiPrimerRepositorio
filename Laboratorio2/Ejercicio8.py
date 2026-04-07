def aplicar_transformacion(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


texto_usuario = input("Ingrese un texto: ")
print("1. Convertir texto a MAYUSCULA")
print("2. Convertir texto a minuscula")
print("3. Convertir primera letra a Mayuscula")

opcion_elegida = int(input("Seleccione un numero del 1 al 3: "))
resultado = aplicar_transformacion(texto_usuario, opcion_elegida)
print(resultado)
