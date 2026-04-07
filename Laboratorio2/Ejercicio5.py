def mostrar_transformacion(palabra, opcion):
    if opcion == 1:
        resultado = palabra.upper()
        return resultado

    elif opcion == 2:
        resultado = palabra.lower()
        return resultado

    elif opcion == 3:
        resultado = palabra.capitalize()
        return resultado

    else:
        return "Opcion invalida"


print(mostrar_transformacion("Inge pongame 10", 4))
