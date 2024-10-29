import random
import os

#Numero a adivinar 
numero_aleatorio = random.randint(1,101)
#Numeros de intentos 
intentos = 8

#funcion para limpiar la terminal 
#Ya sea Windows, Linux o MacOs

def limpiar ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def comprobacion(num):
    global intentos
    
    
    if intentos == 0:
        print (f"Te quedaste sin intentos el numero es {num}")
        return True
    
    numero_usuario = int(input('Elige tu numero de 1 al 100: '))
    
    if num == numero_usuario:
        print(f"Felicidades el numero era {num}")
        return True
    
    elif numero_usuario < num:
        intentos -= 1
        print(f'Te quedas corto el numero es mayor a {numero_usuario}'
              f'\nTe quedan {intentos} intentos')
        return False
    
    elif numero_usuario > num:
        intentos -= 1
        print(f'Te fuiste muy arriba el numero es menor a {numero_usuario}'
              f'\nTe quedan {intentos} intentos')
        return False


while comprobacion(numero_aleatorio) == False:
    comprobacion(numero_aleatorio)
    