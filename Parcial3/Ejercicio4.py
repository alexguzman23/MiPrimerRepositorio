for registro in range(1, 51):

    if registro == 42:
        print(f"ALERTA SEGURIDAD: Brecha detectada en ID {registro}. Abortando...")
        break

    if registro % 3 == 0:
        continue

    print(f"Procesando registro ID: {registro}")
