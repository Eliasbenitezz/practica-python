import os 
import random

def clear_screen():
    """"Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear') 

def get_ramdom_number():
    """Generate a ramdom number between 1 and 100"""
    return random.randint(1, 100)

def get_user_input():
    """Get user input and validate it"""
    while True:
        try:
            user_number = int(input("Adivina el numero del 1 al 100: "))
            if 1 <= user_number <= 100:
                return user_number
            else:
                print("El numero debe estar entre 1 y 100.")
        except ValueError:
            print("Por favor ingrese solo numeros enteros.")

def play_game():
    """Main function to play the game"""
    clear_screen()
    print("Bienvenido al juego de adivina el numero!")
    ramdom_number = get_ramdom_number()
    attempts = 0 
    
    