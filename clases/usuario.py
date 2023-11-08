from clases.ficha import Ficha

class Usuario(Ficha):
    def __init__(self, id_ficha, nombre, apellido, dni, cuil, telefono, mail, fecha_nacimiento, direccion, nombre_usuario, contrasena, rol):
        super().__init__(id_ficha, nombre, apellido, dni, cuil, telefono, mail, fecha_nacimiento, direccion)
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol

    # Getters
    def get_nombre_usuario(self):
        return self.nombre_usuario
    def get_contrasena(self):
        return self.contrasena

    def get_rol(self):
        return self.rol

    # Setters
    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_rol(self, rol):
        self.rol = rol