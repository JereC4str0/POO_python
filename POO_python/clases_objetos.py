# La convencion para nombrar clases es utilizar PascalCase

# class Celular():
  # Clase con atributos estaticos
  # marca = "Samsung"
  # modelo = "S23"
  # camara = "48 MP"


# Instancia de objeto Celular
# Un objeto es una instancia de una clase
# celular1 = Celular()


# Atributos de instancia
# Se definen cuando instanciamos una clase (creamos un objeto)
# Cuando se crea el objeto, lo primero que hace es ejecutarse
# Metodo constructor
# self es como una forma de hacer referencia al mismo objeto
# Los metodos son funciones dentro de clases sirven para definir las acciones que puede hacer nuestro objeto
# para definir un metodo se debe pasar el parametro "self" de esta forma puede auto-referenciarse

class Celular:
  def __init__(self, marca, modelo, camara):
    self.marca = marca 
    self.modelo = modelo 
    self.camara = camara 

  def llamar(self):
    print(f"Estas haciendo un llamado desde un: {self.modelo}")

  def cortar(self):
    print(f"Cortaste la llamada desde un: {self.modelo}")

celular1 = Celular("Samsung","S23","48 MP")
celular2 = Celular("Iphone","15 pro","98 MP")

celular1.llamar()
celular2.cortar()
