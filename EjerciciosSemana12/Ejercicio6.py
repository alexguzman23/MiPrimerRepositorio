# Ejercicio 6: Pide un número del 1 al 7
# y muestra el día de la semana correspondiente. Si no está en el rango,
#  muestra un mensaje de error.
print("1 = Lunes")
print("2 = Martes")
print("3 = Miercoles")
print("4 = Jueves")
print("5 = Viernes")
print("6 = Sabado")
print("7 = Domingo")
dia = int(input("Ingrese un numero del 1 al 7: "))

if dia == 1:
    print("El dia elegido es Lunes")
elif dia == 2:
    print("El dia elegido es Martes")
elif dia == 3:
    print("El dia elegido es Miercoles")
elif dia == 4:
    print("El dia elegido es Jueves")
elif dia == 5:
    print("El dia elegido es Viernes")
elif dia == 6:
    print("El dia elegido es Sabado")
elif dia == 7:
    print("El dia elegido es Domingo")
