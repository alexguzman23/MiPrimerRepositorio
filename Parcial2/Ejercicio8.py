# Ejercicio 8

cancion = """Llegue borracho de amor
Como todas las noches
Tu querrás besarme y llenarme de amor
Sin ningún reproche
Dios mío por qué en otro rostro
La mirada la piel que me vuelve loco
Quisiera ser otro y no poder tampoco
Ser un ebrio de amor"""

contador = cancion.count("a")
cancion_lineas = cancion.splitlines()

print(cancion_lineas)
print("El numero de letras 'A' que aparecen son:", contador)
