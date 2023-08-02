# Crear sistema para una escuela, En este sistema, vamos a tener dos clases principales:
# Persona y Estudiante. 
# La clase persona tendra los atributos de nombre y edad y un metodo que imprima el nombre y la edad de la persona.
# La clase estudiante heredará de la clase persona y tambien tendrá un atributo adicional
# grado y un metodo que imprima el grado del estudiante
# deberas utilizar el super en el metodo de inicializacion (init) para reutilizar el codigo de la clase padre (Persona)
# Luego crea una instancia de la clase estudiante e imprime sus atributos y utiliza metodos para asegurarte de que todo 
# funciona correctamente :)

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
def imp_ed_nom(self):
  print(f"nombre: {self.nombre}")
  print(f"edad: {self.edad}")



class Estudiante(Persona):
  def __init__(self, nombre, edad, grado):
    super().__init__(nombre,edad)
    self.grado = grado
  
  def imp_info(self):
   print(f"nombre: {self.nombre}")
   print(f"edad: {self.edad}")
   print(f"grado: {self.grado}")
    
  
estudiante1 = Estudiante("pepito", 35, "3ero")
estudiante1.imp_info()  

