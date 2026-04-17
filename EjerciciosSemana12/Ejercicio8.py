# Ejercicio 8: Pide tres lados de un triángulo y determina
#  si es equilátero, isósceles o escaleno.

lado1 = int(input("ingresa el lado 1 del triangulo:"))
lado2 = int(input("ingresa el lado 2 del triangulo:"))
lado3 = int(input("ingresa el lado 3 del triangulo:"))

if lado1 == lado2 == lado3:
    print("Su triangulo es equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Su triangulo es isósceles")
else:
    print("Su triangulo es escaleno")
