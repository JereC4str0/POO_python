# es una funcion especial que "decora" a otra 
def decorador(funcion):
  def funcion_modificada():
    print("antes de llamar a la funcion")
    funcion()
    print("despues de llamar a la funcion")
  return funcion_modificada

# def saludo():
#   print("hola mundo")

# saludo_modificado = decorador(saludo) 
# saludo_modificado()

@decorador
# se crea la funcion sobre el decorador
def saludo():
  print("hola como estas?")

saludo() 