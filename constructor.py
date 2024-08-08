
class Restoraunt:

  def __init__(self, nombre, categoria, precio):
    self.nombre = nombre
    self.categoria = categoria
    self.precio = precio

  def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria}, Precio: {self.precio}")

restoraunt = Restoraunt("Pizeria argy", "Comida italiana", 50)
restoraunt.mostrar_informacion()

restoraunt2 = Restoraunt("Hambur argy", "Comida rapida", 20)
restoraunt2.mostrar_informacion()