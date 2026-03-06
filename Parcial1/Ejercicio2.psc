Algoritmo Ejercicio2 
	
	Definir numero1 Como Entero
	Definir sumatotal Como Entero
	
	numero1 = 0
	sumatotal = 0
	
	Repetir 
		
		Escribir " Ingrese numeros positivos "
		Leer numero1
		
		Si numero1 > 0 Entonces
			sumatotal = sumatotal + numero1
		FinSi
		
	Hasta Que numero1 < 0
	
	
	Escribir " La suma de los numeros positivos es:" sumatotal
	
FinAlgoritmo