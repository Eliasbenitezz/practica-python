def contar_vocales(texto):
    VOCALES = ['A', 'E', 'I', 'O', 'U',
    'a', 'e', 'i', 'o', 'u',
    'Á', 'É', 'Í', 'Ó', 'Ú',
    'á', 'é', 'í', 'ó', 'ú']
    numeros_de_vocales = 0
    for i in texto:
        if i in VOCALES:
            numeros_de_vocales += 1
    
    return numeros_de_vocales

print(contar_vocales("Python es genial"))  # Salida esperada: 5
