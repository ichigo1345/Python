#definir una clase llamada Producto con los siguiente atributos:
# - 1d
# - nombre
# - descripcion
# - precio_normal
# - precio_oferta
# 
# siguientes metodos:
# getters/setters segun corresponda
# validaciones:
# precio normal > 0
# precio_oferta < precio_normal
# catidad >=0
# ver_info()
class Producto:
    def __init__(self, id, nombre, descripcion, precio_normal, precio_oferta, cantidad):
        self.__id=id
        self.__nombre=nombre
        self.__descripcion=descripcion
        self.__precio_normal=precio_normal
        self.__precio_oferta=precio_oferta
        self.__cantidad=cantidad
    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_precio_normal(self):
        return self.__precio_normal

    def get_precio_oferta(self):
        return self.__precio_oferta

    def get_cantidad(self):
        return self.__cantidad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_precio_normal(self, precio_normal):
        if precio_normal > 0:
            self.__precio_normal = precio_normal
        else:
            raise ValueError("El precio normal debe ser un número mayor a 0.")

    def set_precio_oferta(self, precio_oferta):
        if 0 <= precio_oferta < self.__precio_normal:
            self.__precio_oferta = precio_oferta
        else:
            raise ValueError("El precio de oferta debe ser mayor o igual a 0 y menor que el precio normal.")
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual a 0.")