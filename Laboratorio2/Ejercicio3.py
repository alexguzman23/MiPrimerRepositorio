texto = input("Ingrese un texto: ")
opcion = int(input("Seleccione un numero del 1 al 3: "))

texto_opcion1 = texto.upper()
texto_opcion2 = texto.lower()
texto_opcion3 = texto.capitalize()

if opcion == 1:
    print(texto_opcion1)

elif opcion == 2:
    print(texto_opcion2)

elif opcion == 3:
    print(texto_opcion3)
