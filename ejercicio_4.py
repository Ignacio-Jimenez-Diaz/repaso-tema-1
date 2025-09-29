def calcular_notas(notas):
    """
    Recibe una lista de números (notas entre 0 y 10).
    Devuelve un dict: {'media': float, 'max': float, 'min': float, 'hay_suspensas': bool}.
    Lanza ValueError si la lista está vacía o alguna nota no está en [0, 10].
    """
    if not isinstance(notas, (list, tuple)):
        raise TypeError("notas debe ser una lista o tupla")
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía")

    # Validación y conversión a float
    limpias = []
    for i, n in enumerate(notas):
        try:
            val = float(n)
        except Exception:
            raise ValueError(f"Nota no numérica en posición {i}: {n}")
        if not (0 <= val <= 10):
            raise ValueError(f"Nota fuera de rango [0,10] en posición {i}: {val}")
        limpias.append(val)

    total = sum(limpias)
    media = total / len(limpias)
    nota_max = max(limpias)
    nota_min = min(limpias)
    hay_suspensas = any(n < 5 for n in limpias)

    if hay_suspensas:
        print("Hay al menos una nota suspensa (< 5).")

    return {
        'media': media,
        'max': nota_max,
        'min': nota_min,
        'hay_suspensas': hay_suspensas
    }
