etiqueta = input("Escriba el código de rastreo (AÑO-CATEGORÍA-PAÍS): ")


if etiqueta:

    categoria = etiqueta[5:-3]
    print("Categoría:", categoria)
    resultado = "Ruta Local" if etiqueta[-2:] == "SV" else "Ruta Internacional"
    print(resultado)

else:
    print("Error: La entrada está vacía. Finalizando programa.")
