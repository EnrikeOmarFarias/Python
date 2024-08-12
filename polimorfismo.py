class Restoraunt:

  def __init__(self, nombre, categoria, precio):
    self.nombre = nombre #Atributo
    self.categoria = categoria
    self.__precio = precio #Default: Public, PROTECTED, PRIVATE

  def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria}, Precio: {self.__precio}") #No va a ser posible modificarlo con PRIVATE __

  def get_precio(self):
    return (self.__precio)

  def set_precio(self, precio):
    self.__precio = precio


#Crear clase hijo de restaurant

class Hotel(Restoraunt):
  def __init__(self, nombre, categoria, precio, alberca):
    super().__init__(nombre, categoria, precio)
    self.alberca = alberca

  #Reescribir un metodo (debe llamarse igual)
  def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria}, Precio: {self.__precio}, alberca: {self.alberca}")
#Agregar un metodo que solo exista en hotel
def get_alberca(self):
  return self.alberca

hotel = Hotel("Hote lito", "5 estrellas", 200)
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)