import os 
import random

def limpiar():
    os.system('cls' if os.name=='nt' else 'clear')
    
def intentos():
    vida = 8
    return vida

def numero_random():
    num_random = random.randint(1,100)
    return num_random

def numero_usuario():
    while True:
        try:
            num_usuario = int(input('Ingrese un número del 1 al 100: '))
            limpiar()
            if 1 <= num_usuario <=100:
                return num_usuario
            else:
                print('Ingresa solo numeros entre 1 y 100.')
                input('Presiona Enter para continuar...')
                limpiar()
        except:
            print('Por favor ingresar solo numeros.')
            input('Presiona Enter para continuar...')
            limpiar()

def game(num_alea, vidas):
    while vidas > 0:
        num_usu = numero_usuario()
        if num_usu == num_alea:
            print('Felicidades haz ganado.')
            input('Presiona Enter para continuar...')
            return
        elif num_usu < num_alea:
            print(f'El numero es mayor a {num_usu}')
        else:
            print(f'El numero es menor a {num_usu}')
        vidas -= 1
        print(f'Te quedan {vidas} vidas.')
        input('Presiona Enter para continuar...')
        limpiar()
    print(f'Perdiste. El número era {num_alea}')

if __name__ == '__main__':
    game(numero_random(), intentos())