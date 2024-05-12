# Practicando programacion orientada a objetos

class carro:
  def  __init__ (self, valor, color, MAXvelocidad, marca ):
    self.valor = valor
    self.color = color
    self.MAXvelocidad = MAXvelocidad
    self.marca = marca 

Car = carro(240.0000, "Amarillo", 377, "Lamborgini huracan" )

class empleados:
  def __init__ (self, nombre, edad, salario,  ):
    self.nombre= nombre
    self.edad= edad
    self.salario=salario

employ= empleados("Carlos", 44, 2.899)


class casa:
  def __init__(self, dimensiones, material, precio):
    self.dimensiones = dimensiones
    self.material = material
    self.precio=precio

House= casa("300x300", "Madera", "1.000.000" )


print(House.precio)
print(Car.valor)
print(employ.salario)


