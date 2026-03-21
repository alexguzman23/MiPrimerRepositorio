serie = "Fullmetal alchemits"

## cada variable tiene un espacio de memoria asignado

## mutabilidad= cuando una variable cambia se pierde la inmutabilidad
## POO
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo
## abstracciones ->
## cafe coscafe
## azucar
## agua
## otros ingredientes
## un objeto es el que toma un modelo y este modelo le da funciones y utiliza sus propiedades

## Leon ->
## tiene ojos
## tiene boca (propiedades)
## esta guapo
#############
# corre (funiciones)
# salta


## Clases
## EStructura de datos


## es una variable que tiene adentro otra variable
## Listas.
## Arrays. -> se inicia a contar desde el 0
## tuplas.
## indices.


# -------------------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(serie) las funciones siempre an a tener parentesis ()
# -------------------------------------------------------------------
##las funciones tienen un espacio
## Scope es donde residen las variables

## Colocar el nombre de la serie como titulo
fmatemu = serie.title()
saludo(serie)
# saludo(fmatemu)
fmaMayusculas = serie.upper()
saludo(fmaMayusculas)
## de programacion Lineal
FullmetalCapitalizer = fmaMayusculas.swapcase().title()
## cuando encadenamos funciones se indica que la salida de la funcion actual
## 3 es la entrada de la siguiente funcion

saludo(FullmetalCapitalizer)

## comparar cadenas de texto
comparar1 = "Alex"
comparar2 = "Alex "

# casefold para comparar y pasar a minusculas
variabletemporal = comparar1.casefold == comparar2.casefold()
comparar = comparar1.casefold() == comparar2.casefold()
# print(comparar)
## casefold nos dara true unicamente si los elementos sin identicos sino nos dara un false

# para verificar si es un numero o un caracter vamos a utilizar isalfa()
clasicas2005 = "Gasolina 2025"
comprarisAlpa = clasicas2005.isalpha()
# print(comprarisAlpa, 2005)
# isalpha nos va dar true si el string que se les esta enviando es unicamente letras

## si lo que quiero es que sea solo numero isalnum

letracancion = "Lo que paso, paso, entre tu y yo"  # no tengo numero
decada = "10"

ejemplo = letracancion.isalnum()
print(ejemplo)
ejemplo = decada.isalnum()
# isalnum verifica si la cadena de texto solo tiene numeros si solo tiene numeros no vas a dar true
# si tiene un solo espacio dara false

# verificar que solo sean digitos
comprobardecadas = decada
