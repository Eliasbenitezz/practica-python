import os


def ingreso (ing):
    global sueldo
    sueldo += ing

def gasto (gas):
    global sueldo
    sueldo -= gas

def limpiar ():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def peticion_de_monto (mensaje):
   while True:
    try:
        monto = float(input(mensaje))
        if monto <= 0:
            print("Por favor ingrese numeros Mayor a 0.")
            input("Enter para continuar.") 
            limpiar()
        else:
            return monto
    except ValueError:
        print("Por favor ingrese solo números.")
        input("Enter para continuar.") 
        limpiar()
        
sueldo = float(input('Ingrese su salario: '))        
limpiar()

while True:

    categoria = input(f"Su Sueldo ahora mismo es de {sueldo:,.2f} Guaranies\n"
                      "Si es Gasto ingrese 'G' \nY si es Ingreso ingrese 'I': ").upper()
    limpiar()
    
    if categoria == 'G':
        monto = peticion_de_monto("Ingrese el monto gastado: ")
        gasto(monto) 
        input("Enter para continuar.") 
        limpiar()
    
    elif categoria == 'I':
        monto = peticion_de_monto("Ingrese el monto Ingresado: ")
        ingreso(monto)
        input("Enter para continuar.") 
        limpiar()
    
    else:
        print("Ingrese solo 'G' para gasto\n'I' para ingreso\n'S' para ver tu saldo: ")
        input("Enter para continuar.") 
        limpiar()
 