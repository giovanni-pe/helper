def inverso_multiplicativo(a, m):
    """
    Encuentra el inverso multiplicativo de 'a' módulo 'm'.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def descifrar_cifrado_afin(texto_cifrado, constante_mult, constante_aditiva, alfabeto):
    """
    Descifra un texto cifrado usando el cifrado afin.

    Args:
        texto_cifrado (str): El texto cifrado.
        constante_mult (int): La constante multiplicativa.
        constante_aditiva (int): La constante aditiva.
        alfabeto (str): El alfabeto utilizado.

    Returns:
        str: El texto descifrado.
    """
    # Tamaño del alfabeto
    modulo = len(alfabeto)
    
    # Crear mapeos de letras a números y viceversa
    letra_a_numero = {letra: idx for idx, letra in enumerate(alfabeto)}
    numero_a_letra = {idx: letra for idx, letra in enumerate(alfabeto)}
    
    # Encontrar el inverso multiplicativo de la constante multiplicativa
    inverso_mult = inverso_multiplicativo(constante_mult, modulo)
    if inverso_mult is None:
        return "No se puede descifrar; no existe inverso multiplicativo."
    
    # Descifrar el texto
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra in letra_a_numero:
            numero = letra_a_numero[letra]
            numero_descifrado = (inverso_mult * (numero - constante_aditiva)) % modulo
            texto_descifrado += numero_a_letra[numero_descifrado]
        else:
            texto_descifrado += letra  # Conservar caracteres no mapeados
    
    return texto_descifrado

# Pedir datos al usuario
texto_cifrado = input("Ingresa el texto cifrado: ").lower()
constante_multiplicativa = int(input("Ingresa la constante multiplicativa (a): "))
constante_aditiva = int(input("Ingresa la constante aditiva (b): "))
modulo = int(input("Ingresa el módulo (por ejemplo, 27 para español, 26 para inglés): "))

# Preguntar si es español o inglés
idioma = input("¿El texto está en español o inglés? (es/en): ").lower()
if idioma == "es":
    alfabeto = "abcdefghijklmnñopqrstuvwxyz "[:modulo]
elif idioma == "en":
    alfabeto = "abcdefghijklmnopqrstuvwxyz "[:modulo]
else:
    print("Idioma no reconocido. Usando alfabeto en inglés por defecto.")
    alfabeto = "abcdefghijklmnopqrstuvwxyz "[:modulo]

# Descifrar el texto
texto_descifrado = descifrar_cifrado_afin(
    texto_cifrado,
    constante_multiplicativa,
    constante_aditiva,
    alfabeto
)

print("Texto descifrado:", texto_descifrado)
