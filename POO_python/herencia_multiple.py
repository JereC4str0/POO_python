# lo que hace la herencia es permitir a la clase hija acceder a todos los metodos de la clase padre


# clase padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


def hablar(self):
    print("Estoy hablando un poco")


# clase hija


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad


def mostrar_habilidad():
    print(f"Mi habilidad es: {self.habilidad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # hereda de persona estas propiedades
        # esto se especifica con super()
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa


# con super le estoy diciendo que muestre la habilidad de la clase padre
# aunque el metodo este sobre-escrito


def presentarse(self):
    return f"{super().mostrar_habilidad()}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


roberto = Artista("Cantar")

# como puedo saber si esta es una subclase?
# si devuelve True es por que lo es
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)
# como saber si un objeto es una instancia de una clase
instancia = isinstance(roberto, Artista)
print(instancia)
