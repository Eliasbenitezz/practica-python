import random
import os

#Numero a adivinar 
numero_aleatorio = random.randint(1,101)


#Numeros de intentos 
intentos = 8

'''funcion para limpiar la terminal 
Ya sea Windows, Linux o MacOs'''

def limpiar ():
    input("Enter para continuar.")
    
    if os.name == 'nt':
        os.system('cls')   #Windows 
    else:
        os.system('clear') #Linux y MacOS 
        
'''Función para comprobar los distintos casos 
y retorna True o False para que el juego siga o no'''

def comprobacion(num):
    global intentos    
    
    if intentos == 0:
        print (f"Te quedaste sin intentos el numero es {num}")
        return True
            
    elif num == numero_usuario:
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

#Le damos un valor a numero de usuario para el manejo de error        
numero_usuario = None

while numero_usuario is None:
    try:
            
        numero_usuario = int(input('Elige tu numero de 1 al 100: '))
        
    except ValueError:
            
        print("Por favor ingresa solo números.")        
        limpiar()
    

while not comprobacion(numero_aleatorio):
    pass 
