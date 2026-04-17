# Ejercicio 1: Pide un número al usuario e indica si es positivo,
# negativo o cero usando if, elif y else.


numero = int(input("Escribe un numero: "))

if numero == 0:
    print("El numero ingresado es cero")
elif numero > 0:
    print("El numero ingresado es positivo")
else:
    print("El numero ingresado es negativo")
