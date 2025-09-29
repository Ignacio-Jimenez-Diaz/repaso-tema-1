def decodificar_sin_re(cadena, mayusculas=True, conservar_espacios=True):
    if not isinstance(cadena, str):
        raise TypeError("Se requiere una cadena")
    invertida = cadena[::-1]
    lista = []
    prev_space = False
    for ch in invertida:
        if ch.isalpha():
            lista.append(ch)
            prev_space = False
        elif conservar_espacios and ch.isspace():
            if not prev_space:
                lista.append(' ')
                prev_space = True
    limpia = ''.join(lista).strip()
    return limpia.upper() if mayusculas else limpia.lower()

