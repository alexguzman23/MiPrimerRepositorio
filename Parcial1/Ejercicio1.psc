Algoritmo Ejercicio1
	
	Definir Nota Como Entero

	Nota = 0
	
	Repetir 
		Escribir " Coloque la nota obtenida (0 al 10) "
		Leer Nota
	Hasta Que Nota >= 0 Y Nota <= 10 
	
	
	Si Nota >= 6 Y Nota <= 10 Entonces
		Escribir " Usted ha sido aprobado "
	FinSi
	
	Si Nota <= 4 Y Nota >= 0 Entonces
		Escribir " Usted ha sido reprobado "
	FinSi
	
	Si Nota = 5 Entonces
		Escribir " Usted debe ir a recuperación "
	FinSi
	
	
FinAlgoritmo
