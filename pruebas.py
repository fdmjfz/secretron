import string
import random


def encriptar(texto, clave):
    letters = string.ascii_letters
    letters = letters + '0123456789.,?:;'

    numerico, nuevo_orden, resultado = [], [], []

    for i in texto:
        numerico.append(letters.find(i))

    numerico = [j for j in numerico if j >= 0]
    random.seed(clave)
    for k in range(0, len(numerico)):
        nuevo_orden.append(random.randint(0, len(numerico)))

    for idx in range(0, len(numerico)):
        new_idx = numerico[idx] + nuevo_orden[idx]
        if new_idx > len(letters):
            new_idx = new_idx - len(letters)

        resultado.append(new_idx)

    encriptado = [letters[m] for m in resultado]

    return '-'.join(encriptado)


def desencriptar(texto, clave):
    letters = string.ascii_letters
    letters = letters + '0123456789.,?:;'
    numerico, viejo_orden, resultado = [], [], []
    for i in texto:
        numerico.append(letters.find(i))

    numerico = [j for j in numerico if j >= 0]
    random.seed(clave)
    for k in range(0, len(numerico)):
        viejo_orden.append(random.randint(0, len(numerico)))

    for idx in range(0, len(numerico)):
        new_idx = numerico[idx] - viejo_orden[idx]
        if new_idx < 0:
            new_idx = len(letters) + new_idx
        resultado.append(new_idx)

    desencriptado = [letters[m] for m in resultado]

    return '-'.join(desencriptado)


texto = "hace dos letraaaas iguaaaaaal?"
clave = 'prueba'


encripted = encriptar(texto, clave)
encripted


desencriptado = desencriptar(encripted, "prueba")
desencriptado
