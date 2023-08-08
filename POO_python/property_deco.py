class Persona:
  def __init__(self, nombre, edad):
    self._nombre = nombre
    self._edad = edad

  @property # esto que esta aca es un setter, no va a ser una funcion, sino una propiedad
  def nombre(self):
   return self._nombre

  @nombre.setter 
  def nombre(self, new_nombre):
    self._nombre = new_nombre
  
  @nombre.deleter
  def nombre(self):
    del self.nombre
    
  
persona = Persona("pepito", 23)
# de esta forma podemos usar la notacion del punto para llamarlo como si fuese una propiedad
nombre = persona.nombre
print(nombre)