import random
from collections import Counter

def generar_adn(n):
    """
    Genera una cadena de ADN aleatoria de longitud n y devuelve (secuencia, conteo_dict).
    Lanza ValueError si n no es entero positivo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un entero no negativo")
    bases = ['A', 'T', 'C', 'G']
    # Generar secuencia usando random.choices para eficiencia
    seq_list = random.choices(bases, k=n)
    secuencia = ''.join(seq_list)
    conteo = dict(Counter(seq_list))
    # Asegurar que todas las bases aparezcan en el diccionario con valor 0 si es necesario
    for b in bases:
        conteo.setdefault(b, 0)
    return secuencia, conteo

