Algoritmo Laboratorio
	
	//Sumar hasta ingresar 5 números mayores que 10 usando "Y"
	
    Definir numero1 Como Entero
    Definir contador Como Entero
    Definir sumatotal Como Entero
    Definir esvalido Como Logico
	
    numero1 = 0
    contador = 0
    sumatotal = 0
	
    Escribir "Ingrese un número mayor a 10 y menor a 100, el programa termina hasta ingresar 5 números."
	
    Mientras contador < 5 
		
        Leer numero1
		esvalido = numero1 > 10 Y numero1 < 100
		
        Si esvalido Entonces
            contador = contador + 1
            sumatotal = sumatotal + numero1
            Escribir "Llevas: ", contador
            Escribir "Ingrese otro número."
        SiNo
            Escribir "Número inválido, intenta de nuevo."
        FinSi
		
    Fin Mientras
	
    Escribir "Se han completado los 5 números mayores a 10."
    Escribir "La suma de estos números es: ", sumatotal
	
FinAlgoritmo
