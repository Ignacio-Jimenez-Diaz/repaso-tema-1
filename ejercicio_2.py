def simulador_ahorro(cantidad_inicial, aporte_mensual, meses):
    if meses < 0:
        raise ValueError("El número de meses no puede ser negativo")
    total = cantidad_inicial + aporte_mensual * meses
    return total

def main():
    try:
        cantidad_inicial = float(input("Cantidad inicial (€): ").strip())
        aporte_mensual = float(input("Aporte mensual (€): ").strip())
        meses = int(input("Número de meses: ").strip())
    except ValueError:
        print("Entrada no válida. Introduce números correctos.")
        return

    total = simulador_ahorro(cantidad_inicial, aporte_mensual, meses)
    print(f"Total ahorrado tras {meses} meses: {total:.2f} €")
    if total > 5000:
        print("¡Felicidades! Has superado los 5000 € de ahorro.")

if __name__ == "__main__":
    main()
