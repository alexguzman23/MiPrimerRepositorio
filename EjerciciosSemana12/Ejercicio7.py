# Ejercicio 7: Solicita el monto de una compra y aplica:
# Más de 100: 20% de descuento
# Entre 50 y 100: 10% de descuento
# Menos de 50: sin descuento

precio = int(input("Ingrese el precio de su articulo: "))

if precio > 100:
    descuento = precio * 0.20
    nuevoprecio = precio - descuento
    print("Su articulo le queda a $", nuevoprecio)
elif precio >= 50 and precio <= 100:
    descuento = precio * 0.10
    nuevoprecio = precio - descuento
    print("Su articulo le queda a $", nuevoprecio)
elif precio < 50:
    print("Su articulo no tiene descuento, sigue a su precio original:", precio)

# otro punto para parcial y solo con if los hago por que es el unico que comprendo
# para que vea no es con ayuda de ia
