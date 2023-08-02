# Crear una clase Estudiante que tenga los atributos Nombre, Edad y Grado 
# Ademas hay que agregar un metodo que se llame "Estudiar" que imprima "El estudiante x esta estudiando" 
# Crear un objeton estudiante y usar el metodo Estudiar 
# Se debe interactuar con el usuario y este debe brindar los atributos
# Al escribir "estudiar" utilizar el metodo estudiar() (no case sensitive)


class Estudiante:
  def	__init__(self, nombre, edad, grado, estudiar):
    self.nombre = nombre
    self.edad	= edad
    self.grado = grado
    self.estudiar = estudiar
  
  def Estudiar(self):
    print(f"El estudiante {self.nombre} está estudiando ")
    

# estudiante1 = Estudiante("Pepito", "83", "3ero")
# estudiante1.Estudiar()

estudiante1 = Estudiante(input("Ingrese su nombre: "),
                         input("Ingrese su edad: "),
                         input("Ingrese grado: "),
                         input("Escriba 'estudiar' si desea comenzar a estudiar: "),)

if estudiante1.estudiar == 'estudiar':
   estudiante1.Estudiar()



