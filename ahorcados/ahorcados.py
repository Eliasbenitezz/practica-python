import random
import os
palabras = ["universidad","computadora","impresora","escritorio"]

palabra_random = random.choice(palabras)

palabra_secreta = ["_"] * len(palabra_random)

intentos = 8

while intentos > 0 and "_" in palabra_secreta:
    print (" ".join(palabra_secreta))
    print (f"Te quedan {intentos} intentos.") 
    
    letra_usuario = input("Ingrese una letra: ").lower()

    if letra_usuario in palabra_random:
        for p, l in enumerate(palabra_random):
            if l == letra_usuario:
                palabra_secreta[p] = letra_usuario
        print ("Correcto!.")
        input("Enter para continuar.")
        os.system("cls")
    else:
        intentos -= 1
        print("Lo siento esa letra no esta en la palabra.")
        input("Enter para continuar.")
        os.system("cls")
if "_" in palabra_secreta:
    print(f"Te quedaste sin Intentos.\n\nLa palabra era: {palabra_random}")
else:
    print(f"Felicidades, adivinaste la palabra: {palabra_random}\nY te sobraron {intentos} intetos")  