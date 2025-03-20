import random 
import os
palabra = random.choice(["universidad","odontologia"])
palabra_oculta =["-"] * len(palabra)
intentos = 8

while intentos > 0 and "-" in palabra_oculta:
    print(f"Te quedan {intentos} Intentos. ") 
    
    print("".join(palabra_oculta)) 
    
    Letra_usuario = input("Ingrese una letra: ").lower()
    
    cantidad_de_letras = len(Letra_usuario)

    if Letra_usuario == palabra:
        break
    elif Letra_usuario in palabra:
        for I, L in enumerate(palabra):
            if L == Letra_usuario:
                palabra_oculta[I] = L
        print("Felicidades haz adivinado")
    elif cantidad_de_letras == 0:
        intentos -= 1
        print(f"Lo siento {Letra_usuario} no esta en la palabra")
    elif cantidad_de_letras > 0:
        intentos -= 1
        print(f"Lo siento {Letra_usuario} no es la palabra")
           
    input("Enter para continuar")
    os.system("cls")

if intentos == 0:
    print(f"Haz perdido, te quedaste sin intentos la palabra era {palabra}")
else:
    print(f"Haz ganado, la palabra era {palabra}") 