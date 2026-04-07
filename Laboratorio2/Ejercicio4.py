def transformar_palabras(lista, opcion):
    resultado = []

    for palabra in lista:
        if opcion == 1:
            resultado.append(palabra.upper())
        elif opcion == 2:
            resultado.append(palabra.lower())
        elif opcion == 3:
            resultado.append(palabra.capitalize())

    return resultado


mis_palabras = ["Hola", "TEngo", "miedO"]

print(transformar_palabras(mis_palabras, 1))
print(transformar_palabras(mis_palabras, 2))
print(transformar_palabras(mis_palabras, 3))
