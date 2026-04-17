# Ejercicio 9: Solicita un año y determina si es bisiesto.

año = int(input("Ingresa un año para saber si es bisiesto: "))

if año % 4 == 0:
    print("Este año si es bisiesto")
else:
    print("No es bisiesto")
