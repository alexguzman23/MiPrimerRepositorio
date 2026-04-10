# Ejercicio 12

texto = "Alexander.txt"

remover_sufijo = texto.removesuffix(".txt")
remover_prefijo = remover_sufijo.removeprefix("ING.")
texto_nuevo = remover_prefijo.upper()

print(texto_nuevo)

## El prefijo no hizo nada ya que ING. no existia pero lo pedia el ejercicio
