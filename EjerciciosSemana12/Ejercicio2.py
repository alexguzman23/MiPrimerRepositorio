# Ejercicio 2: Solicita la edad de una persona y muestra si es menor de edad,
# mayor de edad o adulto mayor (60 o más).

Edad = int(input("Ingrese su edad: "))

if Edad >= 60:
    print("Eres un adulto mayor")
elif Edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
