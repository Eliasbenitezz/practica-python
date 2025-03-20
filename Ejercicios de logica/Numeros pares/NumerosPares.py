
def filtrar_pares(numeros):
    
    numeros_pares = []    
    for i in numeros:
        if i % 2 == 0:
            numeros_pares.append(i)
    return numeros_pares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_pares(lista_numeros))  