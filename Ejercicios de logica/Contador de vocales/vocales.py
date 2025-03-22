def contar_vocales(texto):
    vocales = 'aeiouáéíóú'
    numeros_de_vocales = 0
    for i in texto:
        if i in vocales.upper() or i in vocales.lower():
            numeros_de_vocales += 1
    
    return numeros_de_vocales

print(contar_vocales("Python es genial"))  # Salida esperada: 5
