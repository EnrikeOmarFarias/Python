
class Restoraunt:

  def __init__(self, nombre, categoria, precio):
    self.nombre = nombre #Atributo
    self.categoria = categoria
    self._precio = precio #Default: Public, PROTECTED, PRIVATE

  def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria}, Precio: {self._precio}")

restoraunt = Restoraunt("Pizeria argy", "Comida italiana", 50)
restoraunt.mostrar_informacion()

restoraunt2 = Restoraunt("Hambur argy", "Comida rapida", 20)
restoraunt2.mostrar_informacion()