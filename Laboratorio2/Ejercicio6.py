def transformar_y_contar(texto, opcion):

    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()

    cantidad = len(resultado)
    return resultado, cantidad


texto_final, total = transformar_y_contar("Parangaricutirimícuaro", 1)

print(texto_final)
print(total)
