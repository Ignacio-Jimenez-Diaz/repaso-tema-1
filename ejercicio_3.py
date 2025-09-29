def clasificar_numeros(lista):
    """Devuelve (pares, impares, negativos) a partir de una lista de enteros."""
    pares = []
    impares = []
    negativos = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        if n < 0:
            negativos.append(n)
    return pares, impares, negativos