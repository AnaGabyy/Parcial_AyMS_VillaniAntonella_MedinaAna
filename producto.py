import datetime

class Producto:
    def __init__(self, id_producto, nombre, marca, descripcion, precio, stock, fecha_vencimiento, id_categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.marca = marca
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.fecha_vencimiento = fecha_vencimiento
        self.id_categoria = id_categoria


    # Getters
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_marca(self):
        return self.marca

    def get_descripcion(self):
        return self.descripcion

    def get_precio(self):
        return self.precio

    def get_stock(self):
        return self.stock

    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento

    def get_id_categoria(self):
        return self.id_categoria


    # Setters
    def agregar_id(self, id_producto):
        self.id_producto = id_producto

    def agregar_nombre(self, nombre):
        self.nombre = nombre

    def agregar_marca(self, marca):
        self.marca = marca

    def agregar_descripcion(self, descripcion):
        self.descripcion = descripcion

    def agregar_precio(self, precio):
        self.precio = precio

    def agregar_stock(self, stock):
        self.stock = stock

    def agregar_fecha_vencimiento(self, año, mes, dia):
        self.fecha_vencimiento = datetime.datetime(año, mes, dia)

    def agregar_id_categoria(self, id_categoria):
        self.id_categoria = id_categoria



    def mostrar(self):
        return f"Producto: {self.nombre}, Marca: {self.marca}, Descripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock}, Fecha de vencimiento: {self.fecha_vencimiento}, ID de la categoria: {self.id_categoria}"