# Get obtine un valor y set  agrega un valor 

class Restoraunt:

  def __init__(self, nombre, categoria, precio):
    self.nombre = nombre #Atributo
    self.categoria = categoria
    self.__precio = precio #Default: Public, PROTECTED, PRIVATE

  def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria}, Precio: {self.__precio}") #No va a ser posible modificarlo con PRIVATE __

  def get_precio(self):
    print(self.__precio)

  def set_precio(self, precio):
    self.__precio = precio

restoraunt = Restoraunt("Pizeria argy", "Comida italiana", 50)
restoraunt.mostrar_informacion()
restoraunt.set_precio(100)
restoraunt.get_precio()


restoraunt2 = Restoraunt("Hambur argy", "Comida rapida", 20)
restoraunt2.mostrar_informacion()
restoraunt2.get_precio()

