lecturas = []


print("Por favor, ingrese 5 lecturas de temperatura:")
for i in range(5):
    valor = int(input(f"Lectura {i+1}: "))
    lecturas.append(valor)

print("\n--- Reporte del Sensor ---")


for temp in lecturas:
    match temp:
        case 0:
            print(f"Temperatura {temp}°C -> Alerta: Punto de Congelación")
        case 100:
            print(f"Temperatura {temp}°C -> Alerta: Punto de Ebullición")
        case _:
            # 3. Operador Ternario interno para el caso por defecto
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(f"Temperatura {temp}°C -> {estado}")
