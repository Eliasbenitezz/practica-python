import random
import string

def generador_contraseña (n):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = []
    for i in range(n):
        contraseña.append(random.choice(caracteres))
    return "".join(contraseña)

longitud = int(input("¿Cuantos caracteres deseas que tenga tu contraseña?: "))
contraseña = generador_contraseña(longitud)
print(f"Tu contraseña es: {contraseña}") 