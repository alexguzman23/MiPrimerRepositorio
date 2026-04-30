# SELECT CASE nivel
nivel = input("Nivel (1 o 2): ")

if nivel == "1":
    cartas = ["caballo", "perro", "caballo", "perro"]
    meta = 2  # Se necesitan 2 aciertos para ganar
if nivel == "2":
    cartas = ["caballo", "perro", "gato", "caballo", "perro", "gato"]
    meta = 3  # Se necesitan 3 aciertos para ganar

# 2. FOR cartas
for c in cartas:
    print("Carta lista")

aciertos = 0
continuar = True


while continuar:
    p1 = int(input("Elige una carta del 0 al 3: "))
    p2 = int(input("Elige otra carta del 0 al 3 diferente a la anterior: "))

    carta1 = cartas[p1]
    carta2 = cartas[p2]

    print("Viste:", carta1, "y", carta2)

    if carta1 == carta2:
        print("¡Acierto!")
        aciertos = aciertos + 1
    else:
        print("Mal, intenta de nuevo")

    if aciertos == meta:
        print("¡Ganaste! Encontraste los", meta, "nombres.")
        continuar = False
