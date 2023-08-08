class Auto():
  def __init__(self): # esto es abstraccion, el usuario no sabe el estado del auto
    self._estado = "apagado"
    
  def encender(self):
    self._estado = "encendido"
    print("el auto esta encendido")
    
  def conducir(self):
    if self._estado == "apagado":
      self.encender()
    print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()

 