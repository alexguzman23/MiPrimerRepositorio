# Ejercicio 5: Solicita dos números y una operación (+, -, *, /)
# y realiza el cálculo usando if, elif y else.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
print("1 = Suma ")
print("2 = Resta ")
print("3 = Multiplicacion")
print("4 = Division")
eleccion = int(input("Seleccione un numero: "))

if eleccion == 1:
    print("La suma es", numero1, "+", numero2, "=", numero1 + numero2)
elif eleccion == 2:
    print("La resta es", numero1, "-", numero2, "=", numero1 - numero2)
elif eleccion == 3:
    print("La multiplicacion de", numero1, "x", numero2, "=", numero1 * numero2)
elif eleccion == 4:
    print("La division de", numero1, "÷", numero2, "=", numero1 / numero2)

## Inge punto para el parcial por este ejercicio que hice de largo sin ia
