class Restorant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #Atributo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        
# Instanciar la clase

restaurant = Restorant()
restaurant.agregar_restaurant("Pizzeria argy")
restaurant.mostrar_informacion()

restaurant2 = Restorant()
restaurant2.agregar_restaurant("Lomos argy")
restaurant2.mostrar_informacion()

#Mostra la informacion

print(f"Nombre Restaurant: {restaurant.nombre}")
print(f"Nombre Restaurant: {restaurant2.nombre}")