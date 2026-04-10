# Ejercicio 4

palabra = "CANTANDO"

palabra_minus = palabra.lower()
remover_pala = palabra_minus.removesuffix("ando")
contador_pala = remover_pala.find("t")

print("la palabra en minuscula:", palabra_minus)
print("la palabra sin sufijo es:", remover_pala)
print("La letra T se encuentra en el puesto:", contador_pala)
