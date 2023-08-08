# el encapsulamiento permite ocultar cierta complejidad interna que hay dentro de una clase

class Miclase:
  def __init__(self):
    self._atributo_privado = "valor" # atributo privado
    self.__atributo_muy_privado = "valorsecreto" # atributo muy privado
    
  
objeto = Miclase()
print(object)

# para acceder a un atributo encapsulado se utilizan getters and setters  