class Ficha:

    def __init__(self, id_ficha, nombre, apellido, dni, cuil, telefono, mail, fecha_nacimiento, direccion):
        self.id_ficha = id_ficha
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cuil = cuil
        self.telefono = telefono
        self.mail = mail
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion

    # Getters
    def get_id_ficha(self):
        return self.id_ficha

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_dni(self):
        return self.dni

    def get_cuil(self):
        return self.cuil

    def get_telefono(self):
        return self.telefono

    def get_mail(self):
        return self.mail

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_direccion(self):
        return self.direccion


    # Setters
    def set_id_ficha(self, id_ficha):
        self.id_ficha = id_ficha

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_dni(self, dni):
        self.dni = dni

    def set_cuil(self, cuil):
        self.cuil = cuil

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_mail(self, mail):
        self.mail = mail

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_direccion(self, direccion):
        self.direccion = direccion