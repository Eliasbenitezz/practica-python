def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        if i >= 1:
            factorial *= i 
    return factorial

print(factorial(5))  # Salida esperada: 120 