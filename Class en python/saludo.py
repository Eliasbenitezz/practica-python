class saludo:
    def __init__(self, nombre, apellido, edad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        
        print(f"Hola {nombre} {apellido} me dijeron que tienes {edad} años."
              f"\nY que tu número de telefono es {telefono}") 