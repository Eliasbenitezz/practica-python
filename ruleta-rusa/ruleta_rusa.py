import pathlib
import random
import time
import os 

def limpiar ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def ruleta():
    
    bala= random.randint(1,6)    
    empieza = int(input('''Quien empieza el juego?
1- Diler
2- Vos: '''))
    
    limpiar()
    
    disparo = 1 
    
    while bala >= disparo:
        if empieza == 1:
            print('Es turno del diler')
            time.sleep(2)
            limpiar()
            if bala == disparo:
                print('El diler murio. GANASTE!!')
                input()
                limpiar()
                disparo += 1
            else:
                disparo += 1
                print ('El diler se salva.')
                time.sleep(2)
                limpiar()
                print('Es tu turno, buena suerte')
                input('Enter para disparar.') 
                time.sleep(2)
                if bala == disparo:
                    print('Haz perdido. Ya mamaste')
                    disparo += 1
                    input()
                    
                else:
                    disparo += 1
                    print('Te salvaste, por ahora...')
                    input()
                    limpiar()
                    
        else: 
            print('Es tu turno.')
            input('Enter para disparar.')
            time.sleep(2)
            limpiar()
            if bala == disparo:
                print('Haz perdido. Ya mamaste')
                disparo += 1
                input()
                limpiar()
            else:
                disparo += 1 
                print('Es turno del diler. Te salvaste')
                empieza = 1
                input()
                limpiar()

if __name__ == "__main__":
    ruleta()