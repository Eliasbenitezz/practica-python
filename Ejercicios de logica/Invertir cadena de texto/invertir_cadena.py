def invertir_cadena(texto):
    cadena_invertida = ""
    for i in reversed(texto):
        cadena_invertida += i
    return cadena_invertida

#También se puede hacer 
palabra = 'Hola'
print(palabra[::-1])
cadenaInvertida = invertir_cadena("hola")
print(cadenaInvertida) 