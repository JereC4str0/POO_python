class A:
  def hablar(self):
    print("Hola desde A")

class B(A):
  def hablar(self):
    print("Hola desde B")
    
# C y B heredan de la clase A

class C(A):
  def hablar(self):
    print("Hola desde C")
    
 
# D hereda de dos clases (B y C)   
class D(B,C):
  def hablar(self):
    print("Hola desde D")


# cual va a hablar?
d = D()
d.hablar()

# como la primer clase que herede es B, me va a traer B
# si no encuentra el metodo en B va a buscar en C
# y por ultimo, si no lo encuentra en C se va a buscarlo a A
# se puede ver de forma grafica con el metodo mro()

print(D.mro())

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]