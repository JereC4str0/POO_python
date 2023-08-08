
class Persona:
  def __init__(self, nombre, edad):
    self._nombre = nombre
    self._edad = edad
    
  def get_nombre(self):
    return self._nombre
  
  def set_nombre(self, new_nombre):
    self._nombre = new_nombre
   
   
persona = Persona("Jere", 23)

nombre = persona.get_nombre() 

persona.set_nombre("pepito")

print(nombre)