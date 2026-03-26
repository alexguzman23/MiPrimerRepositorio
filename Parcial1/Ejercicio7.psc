Algoritmo Ejercicio7
	Definir numero1 Como Entero	
	Definir numero2 Como Entero
	
	numero2 = 1
	numero1 = 1
	
	Escribir " Ingrese un numero "
	
	Repetir
		Si numero1 <= 0 Entonces
			Escribir " Debe ingresar un numero mayor a 0 "
		FinSi
		Leer numero1
	Hasta Que numero1 > 0
	
	Escribir " Ingrese otro numero para mostrar su producto y cociente "
	
	Repetir
		Si numero2 <= 0 Entonces
			Escribir " Debe ingresar un numero mayor a 0 "
		FinSi
		Leer numero2
	Hasta Que numero2 > 0
	
	Escribir " El producto de " numero1 " x " numero2 " es " numero1*numero2
	Escribir " La cociente de " numero1 " ÷ " numero2 " es " numero1/numero2
	
FinAlgoritmo
