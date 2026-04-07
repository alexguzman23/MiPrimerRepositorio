def mostrar_transformacion(palabra, opcion):

    if opcion == 1:
        resultado = palabra.upper()

    elif opcion == 2:
        resultado = palabra.lower()

    elif opcion == 3:
        resultado = palabra.capitalize()

    print((resultado))


mostrar_transformacion("Inge pongame 10", 1)
