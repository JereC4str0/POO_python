class Gato():
  def sonido(self):
    return "miau"
  
class Perro():
  def sonido(self):
    return "guau"


def hacer_sonido(animal):
  print(animal.sonido())
  

gato = Gato()
perro = Perro()

print(gato.sonido())
hacer_sonido(perro)

# DUCK TYPING 

# El duck typing es una técnica de tipado dinámico en programación que se enfoca en el comportamiento de los objetos
# en lugar de su tipo explícito. Esto significa que si un objeto se comporta como un pato, podemos tratarlo como un pato,
# sin importar su tipo real. Es una forma flexible y poderosa de programar, presente en lenguajes como Python y Ruby,
# que permite mayor reutilización de código al no depender de herencias o interfaces específicas.




# Enlases dinamicos
# Enlaces estaticos
# tipo real
# tipo declarado 
