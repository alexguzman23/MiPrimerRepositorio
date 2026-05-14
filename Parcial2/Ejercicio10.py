# Ejercicio 10

texto = "Python2026"

solo_let_nume = texto.isalnum()
texto_minuscula = texto.lower()
texto_reemplazo = texto_minuscula.replace("2026", " ")

print("¿Es alfanumerico?", solo_let_nume)
print("Texto en minuscula:", texto_minuscula)
print("Texto sin los numeros:", texto_reemplazo)
