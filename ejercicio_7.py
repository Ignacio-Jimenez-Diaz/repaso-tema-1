from urllib.parse import urlparse

def analizar_url(url):
    url = url.strip()
    if not url:
        raise ValueError("URL vacía")
    if "://" not in url:
        url = "http://" + url
    p = urlparse(url)
    protocolo = p.scheme or None
    dominio = (p.netloc.split('@')[-1].split(':')[0]) or None
    if not dominio:
        raise ValueError("Dominio no encontrado")
    recurso = None
    partes = []
    if p.path and p.path != "/":
        partes.append(p.path.lstrip('/'))
    if p.query:
        partes.append('?' + p.query)
    if p.fragment:
        partes.append('#' + p.fragment)
    if partes:
        recurso = ''.join(partes)
    return {"protocolo": protocolo, "dominio": dominio, "recurso": recurso}
