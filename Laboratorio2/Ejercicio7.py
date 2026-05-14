def transformar_paso_a_paso(texto, lista_opciones):
    resultado = texto

    for opcion in lista_opciones:
        if opcion == 1:
            resultado = resultado.upper()
        elif opcion == 2:
            resultado = resultado.lower()
        elif opcion == 3:
            resultado = resultado.capitalize()

        print(resultado)

    return resultado


transformar_paso_a_paso("Inge con este ejercicio me dio 10 paros y 3 derrames", [1, 3])

## posdata: no ocupe IA bueno un poquito para entender el uso de los "[]" y
## el orden de colocar las lineas
## vi uno que otro videito de la web :))
