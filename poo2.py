


def main():
    class Persona():
        def __init__(self):
            self.nombre = input("ingrese el nombre: ")
            self.apellido = input("ingrese el apellido: ")
            self.direccion = input("ingrese la direccion: ")
            self.telefono = input("ingrese el telefono: ")
            
    
        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}") 

   

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo = float (input("ingrese el sueldo: "))
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0
        
        def mostrarempleados(self):
            super().mostrarPersona()
            print(f"Sueldo: {self.__sueldo}")
            print(f"Transporte: {self.transporte}")
            print(f"alimentacion: {self.alimentacion}")
            print(f"Pension: {self.pension}")
        
    
    empleado1 = Empleado()
    #empleado1.sueldo = 4000000
    empleado1.mostrarempleados()






if __name__=="__main__":
    main()