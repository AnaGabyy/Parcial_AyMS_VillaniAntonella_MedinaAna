from clases.ficha import Ficha

class Usuario(Ficha):
    def __init__(self, id_ficha, nombre, apellido, dni, cuil, telefono, mail, fecha_nacimiento, direccion, contrasena, rol):
        super().__init__(id_ficha, nombre, apellido, dni, cuil, telefono, mail, fecha_nacimiento, direccion)
        self.contrasena = contrasena
        self.rol = rol

    # Getters
    def get_contrasena(self):
        return self.contrasena

    def get_rol(self):
        return self.rol

    # Setters
    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_rol(self, rol):
        self.rol = rol