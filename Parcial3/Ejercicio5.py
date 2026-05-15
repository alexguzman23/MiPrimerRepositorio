nombre_completo = input("Ingrese su nombre y apellido: ")


palabras = nombre_completo.split()
palabras_invertidas = palabras[::-1]


for palabra in palabras_invertidas:

    letras_formateadas = []

    for letra in palabra:

        letras_formateadas.append(letra)

    print(".".join(letras_formateadas))
