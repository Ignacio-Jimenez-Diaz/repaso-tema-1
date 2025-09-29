def inventario_personajes(personajes):
    """
    Recibe dict {nombre: tipo}.
    Devuelve (lista_humanos, lista_criaturas).
    Lista de humanos ordenada alfabéticamente.
    Lista de criaturas ordenada por longitud de nombre ascendente.
    Lanza TypeError si la entrada no es un dict.
    """
    if not isinstance(personajes, dict):
        raise TypeError("personajes debe ser un diccionario")

    humanos = []
    criaturas = []
    for nombre, tipo in personajes.items():
        if isinstance(tipo, str) and tipo.lower() == "humano":
            humanos.append(nombre)
        elif isinstance(tipo, str) and tipo.lower() == "criatura":
            criaturas.append(nombre)
        else:
            # Ignorar entradas con tipo desconocido
            continue

    humanos.sort(key=lambda s: s.lower())
    criaturas.sort(key=lambda s: (len(s), s.lower()))
    return humanos, criaturas
