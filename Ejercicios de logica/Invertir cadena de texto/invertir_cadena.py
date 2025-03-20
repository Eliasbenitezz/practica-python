def invertir_cadena(texto):
    cadena_invertida = ""
    for i in reversed(texto):
        cadena_invertida += i
    return cadena_invertida

print(invertir_cadena("hola")) 